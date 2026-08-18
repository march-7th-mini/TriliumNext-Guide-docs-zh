#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trilium 目录导出格式翻译器 v4.1(两阶段 + 增量同步)
===================================================
输入: 上游仓库已 checkout 的三个 Trilium 目录导出树
      docs/Developer Guide, docs/Release Notes, docs/User Guide

阶段一 --init(建骨架):
  - 把英文整包拷贝为骨架(正文先保留原文)
  - 批量翻译所有笔记标题(短文本,便宜)
  - 为每个笔记生成稳定新 ID(_zh_xxx)并持久化
  - 写入属性: #originalHelpNoteId=_help_<源noteId>  #helpDoc=zh
  完成后即可先提交 PR,review 树结构和标题。

阶段二 --translate(默认,翻正文):
  - 增量翻译正文(hash 对比,只翻变化的/未翻译的)
  - 标题与 ID 全部复用 init 阶段的成果

用法:
  python3 translate_trilium_Guide_docs_CHS.py --init            # 初始化(可反复跑,增量)
  python3 translate_trilium_Guide_docs_CHS.py                   # 翻译正文(可反复跑,增量)
  LLM_DRY_RUN=1 python3 translate_trilium_Guide_docs_CHS.py     # 试跑:不调 API

v4.1 变更(2026-08-16):
  - 恢复 verify_output_matches_src() 到 done 判定:
    v4.0 误删此检查,导致旧版译文骗过 hash+含中文轻量检查 → 永远跳过 → 漏翻。
    重新加入「源文全部 reference-link href ⊂ 译文」+「译文长度 ≥ 源文 30%」两条强校验。
  - 新增 output_hash 字段: 翻译成功后记录译文文件的 sha256,
    下次运行时对比磁盘译文哈希。若 state 与译文来自不同分支(分支不同步),
    output_hash 不匹配 → 强制重翻,杜绝「state 说了 done 但译文是旧的」幽灵 bug。
  - 已有 state 条目(无 output_hash): 首次 v4.1 运行只做 verify_output_matches_src 校验,
    通过的补写 output_hash,不通过的标记重翻。不影响性能(纯本地文件对比,无 API 调用)。

v4.0 变更(2026-08-16):
  - 新增 cleanup_orphans(): 处理完成后删除 docs-zh/ 中上游已删除的孤儿文件 + 清理过期 state 条目
    修复 Bug 3: 上游删除文档后旧译文残留,错误地出现在 PR 中
  - 改进 migrate_state(): hash 不匹配时也保留旧 ID 和中文标题,只标记需要重翻
    修复 Bug 2: 迁移失败时丢失 ID/标题导致不必要重翻 + 重复 API 调用
  - state key 全面路径化: 确保所有 key 都是路径形式(Developer Guide/xxx.md)
    杜绝 14 个跨目录同名文件 hash 张冠李戴
  - 简化 done 判定: 不再依赖 verify_output_matches_src 防分支不同步
    (工作流改为整体恢复 docs-zh/ 目录,state 和 output 始终同步)
    保留含中文 + 翻译腔检查作为轻量安全网

v3.3 变更:
  - 新增 verify_output_matches_src:done 判定不再只信 hash+含中文,
    还要求输出包含源文件全部 reference-link href、长度不低于源文 30%。
"""
import argparse
import hashlib
import json
import os
import random
import re
import string
import sys
import time
import urllib.request
import urllib.error

# ====== 配置 ======
MODEL = "deepseek-v4-flash"                  # OpenAI 改成 "gpt-4o-mini"
BASE_URL = "https://api.deepseek.com"        # OpenAI 改成 "https://api.openai.com/v1"
SRC_TREES = [                                # 要翻译的源树(相对仓库根)
    "docs/Developer Guide",
    "docs/Release Notes",
    "docs/User Guide",
]
OUT_DIR = "docs-zh"                          # 输出根目录
STATE_FILE = os.path.join(OUT_DIR, ".translated.json")
MAX_CHARS = 60000                            # 超过此长度的正文跳过,提示手动处理
TITLE_BATCH = 30                             # 标题批量翻译,每批个数(调小防超限)
MAX_OUTPUT_TOKENS = 16000                    # Responses 输出预算(reasoning 也占额度)
REASONING_EFFORT = "none"                    # 关闭思维链(翻译不需要推理);若 API 报 400,改成 None
GLOSSARY_FILE = "glossary.tsv"               # Weblate 术语表(可选,不存在则跳过)
GLOSSARY_INJECT = 60                         # prompt 中最多注入的术语条数
MIN_OUT_LEN_RATIO = 0.3                      # 输出/源长度下限;低于此值判为截断/只翻开头
# ==================

GLOSSARY = {}

API_KEY = os.environ.get("LLM_API_KEY", "")
DRY_RUN = os.environ.get("LLM_DRY_RUN") == "1"

_ID_CHARS = string.ascii_letters + string.digits

def log(msg):
    print(msg, flush=True)

def read_glossary(path=GLOSSARY_FILE):
    """读 Weblate 导出的术语表(英文<TAB>中文),返回 {en: zh};不存在时返回空 dict。"""
    if not os.path.exists(path):
        log(f"[术语表] 未找到 {path},跳过术语注入")
        return {}
    gloss = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or "\t" not in line:
                continue
            en, zh = line.split("\t", 1)
            en, zh = en.strip(), zh.strip()
            if en and zh:
                gloss[en] = zh
    log(f"[术语表] 已加载 {len(gloss)} 条术语(注入前 {GLOSSARY_INJECT} 条)")
    return gloss

def glossary_prompt_block(gloss, limit=GLOSSARY_INJECT):
    """把术语表拼成 prompt 片段;为空时返回空字符串。"""
    if not gloss:
        return ""
    lines = "\n".join(f"{en} → {zh}" for en, zh in list(gloss.items())[:limit])
    return "\n\n[术语表:以下术语翻译时必须使用表中中文,不得自行另译]\n" + lines

def gen_id(used):
    while True:
        nid = "_zh_" + "".join(random.choice(_ID_CHARS) for _ in range(8))
        if nid not in used:
            used.add(nid)
            return nid

def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def str_hash(s):
    """对字符串做 sha256(用于标题变化检测)。"""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def contains_chinese(s):
    """判断文本是否含中文字符,用于识别"假成功"翻译(模型直接返回英文原文)。"""
    return any('\u4e00' <= ch <= '\u9fff' for ch in s)

def has_translation_chatter(s):
    """检测 LLM 假成功套话(旧版模型吐的翻译腔开头,如"好的,这是您要求的…")。
    这类输出含中文但内容张冠李戴/不完整,必须强制重翻。"""
    head = s[:300]
    if "好的，这是您要求的" in head:
        return True
    return bool(re.search(r"以下.{0,20}简体中文翻译", head))

def verify_output_matches_src(src_text, out_text):
    """校验译文输出是否对应当前源文件版本(防漏更新/旧版输出骗过增量检测)。

    背景:state 的 hash 被写成新版、但磁盘上的翻译输出还是旧版内容时,
    仅靠 hash+含中文 的 done 判定会把文件永远判为"已完成",上游再更新也不重翻。

    两条强校验(正常翻译必然通过,旧版/截断输出必然失败):
      1) 输出必须包含源文全部 <a class="reference-link" href="..."> 的 href
         (翻译要求 href 一字不改;源文新增了链接而输出没有 → 输出是旧版)
      2) 输出长度不得低于源文的 MIN_OUT_LEN_RATIO(中文普遍比英文短,
         低于 30% 说明模型只翻了开头或输出被截断)
    """
    src_links = set(re.findall(r'<a class="reference-link" href="([^"]+)"', src_text))
    out_links = set(re.findall(r'<a class="reference-link" href="([^"]+)"', out_text))
    if not src_links.issubset(out_links):
        return False
    if len(out_text) < len(src_text) * MIN_OUT_LEN_RATIO:
        return False
    return True

MARKDOWN_EXTS = {".md", ".markdown"}

def is_markdown(path):
    """判断是否为 Markdown 文档:只有 .md 才翻译正文,代码/资源文件原样拷贝。"""
    return os.path.splitext(path)[1].lower() in MARKDOWN_EXTS

def extract_response_text(data):
    """从 Responses API 返回里提取纯文本,跳过 reasoning 等非文本项。"""
    texts = []
    for item in data.get("output") or []:
        if item.get("type") != "message":
            continue
        for part in item.get("content") or []:
            if part.get("type") == "output_text":
                texts.append(part.get("text", ""))
    if texts:
        return "\n".join(texts).strip()
    if data.get("output_text"):
        return data["output_text"].strip()
    # 失败诊断:输出被截断时给出可操作提示
    hint = ""
    if data.get("status") == "incomplete" and (data.get("incomplete_details") or {}).get("reason") == "max_output_tokens":
        hint = ("(输出被 max_output_tokens 截断:模型把预算花在了 reasoning 上。"
                "请调大 MAX_OUTPUT_TOKENS,或确认 REASONING_EFFORT = \"none\" 生效)")
    raise SystemExit(f"[API 失败] Responses 返回里没有 output_text {hint}: {json.dumps(data, ensure_ascii=False)[:400]}")

def call_api(prompt, max_tokens=MAX_OUTPUT_TOKENS, retries=3):
    """调用 LLM Responses API,返回纯文本回复。"""
    body = {
        "model": MODEL,
        "input": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_output_tokens": max_tokens,
    }
    if REASONING_EFFORT:
        body["reasoning"] = {"effort": REASONING_EFFORT}
    req = urllib.request.Request(
        BASE_URL + "/responses",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
    )
    last_err = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.load(resp)
            return extract_response_text(data)
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')}"
            if e.code in (429, 500, 502, 503):
                time.sleep(5 * (attempt + 1))
                continue
            break
        except Exception as e:
            last_err = str(e)
            time.sleep(5 * (attempt + 1))
    raise SystemExit(f"[API 失败] {last_err}")

def translate_text(text, gloss=None):
    """翻译整篇正文。"""
    term_block = glossary_prompt_block(gloss or GLOSSARY)
    prompt = (
        "你是一位专业的技术文档翻译。请把下面的英文 Markdown 文档翻译成简体中文。\n"
        "要求:\n"
        "1. 忠实原文,不增删内容\n"
        "2. 完整保留 Markdown 结构:标题层级、代码块、表格、列表、图片、加粗斜体\n"
        "3. 完整保留 HTML 标签,尤其是 <a class=\"reference-link\" href=\"...\"> 的 href 值一字不改;若链接锚文本是 [missing note],按 href 里的文件名翻译成中文笔记名(如 Math%20Equations → 数学公式),绝不要输出\"缺失笔记\"\n"
        "4. 代码块里的代码和英文命令不要翻译\n"
        "5. 专有名词保留英文:Trilium、Markdown、GitHub、API、pnpm 等\n"
        "6. 术语全文保持一致"
        + term_block
        + "\n\n7. 只输出译文本身,不要任何解释\n"
        "8. 术语必须与术语表一致:术语表里出现过的英文一律用表中中文,不确定时优先查术语表\n\n"
        "===== 开始 ====="
    ) + "\n\n" + text
    return call_api(prompt)

def translate_titles_batch(items, gloss=None):
    """批量翻译标题。items: [(noteId, title), ...],返回 {noteId: 中文标题}。"""
    if not items:
        return {}
    if DRY_RUN:
        return {nid: title for nid, title in items}

    mapping = {}
    for i in range(0, len(items), TITLE_BATCH):
        batch = items[i:i + TITLE_BATCH]
        obj = {nid: title for nid, title in batch}
        term_block = glossary_prompt_block(gloss or GLOSSARY)
        prompt = (
            "你是专业的技术文档翻译。以下是 Trilium 帮助文档的笔记标题列表"
            "(JSON 对象: 英文标题 → noteId)。请把每个标题翻译成简体中文。\n"
            "要求:\n"
            "1. 保持简洁,通常不超过 30 个汉字\n"
            "2. 专有名词保留英文:Trilium、Markdown、GitHub、API、AI 等\n"
            "3. 版本号、括号内容、& 符号原样保留\n"
            "4. 只返回一个 JSON 对象 {\"noteId\": \"中文标题\"},不要任何解释或代码块标记"
            + term_block
            + "\n\n5. 标题中的术语必须与术语表一致,术语表里出现过的英文一律用表中中文\n\n"
            "标题列表:\n" + json.dumps(obj, ensure_ascii=False)
        )
        reply = call_api(prompt)
        # 去掉可能的 ```json 围栏
        reply = re.sub(r"^```(?:json)?\s*|\s*```$", "", reply.strip())
        try:
            parsed = json.loads(reply)
        except Exception as e:
            log(f"  [警告] 标题批量返回解析失败({e}),本批 {len(batch)} 个标题用原文")
            parsed = {}
        for nid, title in batch:
            zh = parsed.get(nid)
            if isinstance(zh, str) and zh.strip() and zh.strip() != title:
                mapping[nid] = zh.strip()
        log(f"  [标题] 批量 {i // TITLE_BATCH + 1}: 翻译 {len(batch)} 个")
        time.sleep(0.3)
    return mapping

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def iter_nodes(root, path=""):
    """深度优先遍历,产出 (node, 标题路径)。"""
    yield root, path
    for c in root.get("children") or []:
        yield from iter_nodes(c, path + "/" + (root.get("title") or ""))

def state_key(node):
    """节点的 state 键:优先用源文件相对路径(带目录,防跨目录同名文件互相覆盖);
    无正文(book 容器)用 meta:noteId。"""
    if node.get("dataFileName"):
        return node.get("_src_path") or node["dataFileName"]
    return "meta:" + node.get("noteId", "")

def assign_src_paths(node, src_dir):
    """递归给每个有正文的节点标注 _src_path(相对 docs/ 的源文件路径,用于 state key)。"""
    if node.get("dataFileName"):
        node["_src_path"] = os.path.relpath(os.path.join(src_dir, node["dataFileName"]), "docs")
    child_dir = os.path.join(src_dir, node.get("dirFileName") or "")
    for c in node.get("children") or []:
        assign_src_paths(c, child_dir)

def migrate_state(state, meta):
    """旧版 state 用裸文件名做 key,跨目录同名文件互相覆盖(hash 张冠李戴)。
    迁移为带路径 key。

    v4.0 改进:hash 不匹配时也保留旧 ID 和中文标题,只标记需要重翻。
    这样不会丢失已翻译的标题和已生成的 ID,减少不必要的 API 调用。
    """
    migrated = 0
    preserved = 0
    for root in meta.get("files", []):
        for node, _path in iter_nodes(root):
            if not node.get("dataFileName"):
                continue
            new_key = node.get("_src_path")
            if not new_key or new_key in state:
                continue
            rec = state.get(node["dataFileName"])
            if not rec:
                continue
            src_path = os.path.join("docs", new_key)
            if os.path.exists(src_path) and rec.get("hash") == file_hash(src_path):
                # hash 匹配:文件未变化,完整迁移
                state[new_key] = rec
                state.pop(node["dataFileName"], None)
                migrated += 1
            elif rec.get("status") in ("done", "too_big", "code", "suspect"):
                # hash 不匹配:上游改了内容,保留旧 ID 和中文标题,标记需要重翻
                new_rec = dict(rec)
                new_rec["status"] = "pending"
                new_rec.pop("hash", None)  # 清掉旧 hash,build_tree 会检测到需要重翻
                state[new_key] = new_rec
                state.pop(node["dataFileName"], None)
                preserved += 1
    return migrated, preserved

# ============ 阶段一:init(建骨架) ============

def init_phase(meta, state, used_ids, stats):
    """建骨架:翻译标题、生成 ID、拷贝正文原文、写属性。返回 (根节点列表, 是否首次)。"""
    roots = []

    # 1) 收集全部节点:决定哪些标题要翻译、哪些 ID 要生成
    nodes = []
    for root in meta.get("files", []):
        nodes.extend(iter_nodes(root))

    # 2) 标题翻译:只处理 标题变了 / 从没翻译过 的
    need_titles = []
    title_mapping = {}
    for node, _ in nodes:
        key = state_key(node)
        rec = state.get(key, {})
        en_title = node.get("title", "")
        if rec.get("title_hash") != str_hash(en_title):
            need_titles.append((node.get("noteId", ""), en_title))
    if need_titles:
        log(f"[init] 需要翻译标题 {len(need_titles)} 个")
        title_mapping = translate_titles_batch(need_titles, GLOSSARY)
    else:
        log("[init] 标题全部已翻译,无变化")

    # 3) 生成/复用 ID,更新 state
    for node, _ in nodes:
        key = state_key(node)
        rec = state.get(key, {}) or {}
        nid = rec.get("id") or gen_id(used_ids)
        used_ids.add(nid)
        en_title = node.get("title", "")
        zh_title = title_mapping.get(node.get("noteId", "")) or rec.get("title") or en_title
        rec["id"] = nid
        rec["title"] = zh_title
        rec["title_hash"] = str_hash(en_title)
        if node.get("dataFileName"):
            rec.setdefault("status", "pending")   # 正文尚未翻译
        state[key] = rec

    # 4) 拷贝正文原文 + 生成新树(标题/ID/属性)
    for root in meta.get("files", []):
        roots.append(build_tree(root, meta, state, used_ids, stats, translate_body=False))
    return roots

# ============ 阶段二:translate(翻正文) ============

def translate_phase(meta, state, used_ids, stats):
    """翻译正文(增量)。"""
    roots = []
    for root in meta.get("files", []):
        roots.append(build_tree(root, meta, state, used_ids, stats, translate_body=True))
    return roots

# ============ 共用:建树 ============

def build_tree(node, meta, state, used_ids, stats, translate_body):
    """递归构建翻译树:标题/ID/属性从 state 取,正文按阶段处理。"""
    out = dict(node)

    # 标题 & ID
    key = state_key(node)
    rec = state.get(key, {}) or {}
    out["title"] = rec.get("title") or node.get("title", "")
    out["noteId"] = rec.get("id") or node.get("noteId", "")
    used_ids.add(out["noteId"])

    # 正文
    data_fn = node.get("dataFileName")
    src_base = node.get("_src_base", "")
    dst_base = node.get("_dst_base", "")
    if data_fn and src_base:
        src_path = os.path.join(src_base, data_fn)
        dst_path = os.path.join(dst_base, data_fn)
        if os.path.exists(src_path):
            cur_hash = file_hash(src_path)
            rec = state.get(key, {}) or {}
            done = rec.get("status") in ("done", "too_big", "code") and rec.get("hash") == cur_hash
            if not os.path.exists(dst_path):
                done = False
            elif done:
                # v4.1: 验证 output_hash —— 检测 state 与译文文件分支不同步
                # 旧 Bug: 工作流恢复时 state(含新 hash)与译文文件(旧翻译)来自不同来源,
                # hash 匹配 + 含中文 → 错误跳过,译文永远过时(幽灵 bug)。
                _out_hash = rec.get("output_hash")
                if _out_hash and file_hash(dst_path) != _out_hash:
                    log(f"  [修正] {dst_path} 译文文件与 state 记录不同步(output_hash 不匹配),本次重新翻译")
                    done = False
                elif rec.get("status") == "done":
                    # v4.1: 恢复内容强校验(防旧版译文骗过 hash+中文轻量检查)
                    if not is_markdown(dst_path):
                        log(f"  [修正] {dst_path} 是代码文件,强制用上游原文覆盖")
                        done = False
                    else:
                        try:
                            with open(dst_path, encoding="utf-8", errors="ignore") as _f:
                                _out = _f.read()
                            with open(src_path, encoding="utf-8", errors="ignore") as _f:
                                _src = _f.read()
                            if not _src.strip():
                                pass  # 源文件为空(占位节点),跳过 suspect 检查
                            elif os.path.basename(src_path) == "License.md":
                                pass  # License.md 保留英文原文,不翻译,跳过 suspect 检查
                            elif not _out or not contains_chinese(_out) or has_translation_chatter(_out):
                                log(f"  [修正] {dst_path} 输出疑似假成功翻译(纯英文/翻译腔套话),本次重新翻译")
                                done = False
                            elif not verify_output_matches_src(_src, _out):
                                log(f"  [修正] {dst_path} 译文内容与源文不匹配(疑似旧版/截断),本次重新翻译")
                                done = False
                        except OSError:
                            done = False
            if translate_body and not done:
                _translate_body_file(src_path, dst_path, state, key, cur_hash, stats)
            elif not translate_body:
                # init 阶段:已翻译且源未变的保留中文,绝不覆盖
                if done:
                    stats["skipped"] += 1
                else:
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    with open(src_path, "rb") as fi, open(dst_path, "wb") as fo:
                        fo.write(fi.read())
                    stats["copied"] += 1
            else:
                stats["skipped"] += 1
        else:
            log(f"  [警告] 正文文件不存在: {src_path}")

    # 附件
    if src_base:
        out["attachments"] = copy_attachments(src_base, dst_base, node)

    # 属性:保留全部 + 追加两个标签
    attrs = [dict(a) for a in (node.get("attributes") or [])]
    max_pos = max((a.get("position", 0) for a in attrs), default=0)
    attrs.append({"type": "label", "name": "originalHelpNoteId",
                  "value": "_help_" + node.get("noteId", ""),
                  "isInheritable": False, "position": max_pos + 10})
    attrs.append({"type": "label", "name": "helpDoc",
                  "value": "zh", "isInheritable": False, "position": max_pos + 20})
    out["attributes"] = attrs

    # 子节点
    out["children"] = []
    for c in node.get("children") or []:
        c = dict(c)
        c["_src_base"] = os.path.join(src_base, node.get("dirFileName") or "") if node.get("dirFileName") else src_base
        c["_dst_base"] = os.path.join(dst_base, node.get("dirFileName") or "") if node.get("dirFileName") else dst_base
        out["children"].append(build_tree(c, meta, state, used_ids, stats, translate_body))

    out.pop("_src_base", None)
    out.pop("_dst_base", None)
    out.pop("_src_path", None)   # ← 防止内部字段泄漏到输出 !!!meta.json
    return out

def _translate_body_file(src_path, dst_path, state, key, cur_hash, stats):
    """翻译单个正文文件。"""
    with open(src_path, encoding="utf-8", errors="replace") as f:
        content = f.read()

    # License.md: 保留英文原文不翻译,直接拷贝并标记 done
    if os.path.basename(src_path) == "License.md":
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(content)
        rec = state.get(key, {}) or {}
        rec["hash"] = cur_hash
        rec["output_hash"] = file_hash(dst_path)
        rec["status"] = "done"
        state[key] = rec
        stats["copied"] += 1
        log(f"  [跳过-License] {src_path}")
        return

    if not is_markdown(src_path):
        # 代码/资源文件:原样拷贝,不翻译(LLM 会把代码包进代码围栏,污染输出)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(content)
        rec = state.get(key, {}) or {}
        rec["hash"] = cur_hash
        rec["output_hash"] = file_hash(dst_path)
        rec["status"] = "code"
        state[key] = rec
        stats["copied"] += 1
        log(f"  [代码文件-拷贝] {src_path}")
        return

    if not content.strip():
        # 空源文件:直接拷贝为空,不调 LLM(避免幻觉垃圾)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write("")
        rec = state.get(key, {}) or {}
        rec["hash"] = cur_hash
        rec["output_hash"] = file_hash(dst_path)
        rec["status"] = "done"
        state[key] = rec
        stats["copied"] += 1
        log(f"  [空源-拷贝] {src_path}")
        return

    if len(content) > MAX_CHARS:
        log(f"  [跳过-太大] {src_path} ({len(content)} 字符)")
        translated = content
        stats["too_big"] += 1
    else:
        if DRY_RUN:
            translated = content
        else:
            log(f"  [翻译] {src_path} ...")
            translated = translate_text(content, GLOSSARY)
            # 输出校验:必须含中文且不带翻译腔套话,否则判定"假成功",重试 1 次
            if not contains_chinese(translated) or has_translation_chatter(translated):
                log(f"  [重试] 输出不含中文或带翻译腔套话(疑似假成功),重试 1 次: {src_path}")
                translated = translate_text(content, GLOSSARY)
            if not contains_chinese(translated) or has_translation_chatter(translated):
                log(f"  [警告] 两次输出均不合格,标记 suspect,下次运行会重翻: {src_path}")
                rec = state.get(key, {}) or {}
                rec["hash"] = cur_hash
                rec["output_hash"] = file_hash(dst_path)
                rec["status"] = "suspect"
                state[key] = rec
                stats["suspect"] += 1
                return
            # 内容强校验:译文必须保留源文全部链接、长度不低于下限,否则重试一次
            if not verify_output_matches_src(content, translated):
                log(f"  [重试] 输出缺链接或内容不完整(疑似旧版/截断),重试 1 次: {src_path}")
                translated = translate_text(content, GLOSSARY)
                if not verify_output_matches_src(content, translated):
                    log(f"  [警告] 两次输出均未通过内容校验,标记 suspect,下次运行会重翻: {src_path}")
                    rec = state.get(key, {}) or {}
                    rec["hash"] = cur_hash
                    rec["output_hash"] = file_hash(dst_path)
                    rec["status"] = "suspect"
                    state[key] = rec
                    stats["suspect"] += 1
                    return
            time.sleep(0.5)
        stats["translated"] += 1

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(translated)
    rec = state.get(key, {}) or {}
    rec["hash"] = cur_hash
    rec["output_hash"] = file_hash(dst_path)
    rec["status"] = "done"
    state[key] = rec


# ============ 链接锚文本修复(防 [missing note] 被字面翻译) ============

def fix_missing_anchors(root_dir):
    """修复 <a class="reference-link" href="X">[缺失笔记]/[missing note]</a>:
    目标译文文件存在时,用其第一行 # 标题回填锚文本(幂等,可反复跑)。
    目标文件不存在(真缺失)时保持占位,不强行脑补。"""
    import urllib.parse
    pat = re.compile(
        r'(<a class="reference-link" href=")([^"]+)(">)(?:\[缺失笔记\]|\[missing note\])(</a>)',
        re.IGNORECASE,
    )
    fixed = 0
    checked = 0
    for dirpath, _, files in os.walk(root_dir):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding="utf-8") as f:
                content = f.read()
            if "[缺失笔记]" not in content and "missing note" not in content:
                continue
            def repl(m):
                nonlocal fixed
                href = urllib.parse.unquote(m.group(2))
                target = os.path.normpath(os.path.join(os.path.dirname(path), href))
                # 防越界:目标必须仍在 root_dir 内
                if not target.startswith(os.path.abspath(root_dir)):
                    return m.group(0)
                if os.path.exists(target):
                    with open(target, encoding="utf-8") as tf:
                        title = tf.readline().lstrip("#").strip()
                    if title:
                        fixed += 1
                        return f"{m.group(1)}{m.group(2)}{m.group(3)}{title}{m.group(4)}"
                return m.group(0)
            new = pat.sub(repl, content)
            if new != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new)
                checked += 1
    log(f"[锚文本] 检查 {checked} 个文件,回填 {fixed} 个 [缺失笔记] 链接")


def copy_attachments(src_base, dst_base, node):
    """复制附件文件(与正文同目录)。返回新 attachments 数组。"""
    atts = node.get("attachments") or []
    new_atts = []
    for a in atts:
        fn = a.get("dataFileName")
        if not fn:
            new_atts.append(a)
            continue
        s = os.path.join(src_base, fn)
        d = os.path.join(dst_base, fn)
        if os.path.exists(s):
            os.makedirs(os.path.dirname(d), exist_ok=True)
            with open(s, "rb") as fi, open(d, "wb") as fo:
                fo.write(fi.read())
            new_atts.append(a)
        else:
            log(f"  [警告] 附件文件不存在: {s}")
            new_atts.append(a)
    return new_atts

def load_meta(tree_dir):
    with open(os.path.join(tree_dir, "!!!meta.json"), encoding="utf-8") as f:
        return json.load(f)


# ============ v4.0 新增:孤儿文件清理 ============

def collect_expected_outputs(meta, tree, dst_base):
    """递归收集一棵树中所有应该在 docs-zh/ 里存在的文件绝对路径。"""
    expected = set()
    # !!!meta.json 本身
    expected.add(os.path.abspath(os.path.join(dst_base, "!!!meta.json")))

    def _collect(node, src_base, dst_base):
        data_fn = node.get("dataFileName")
        if data_fn:
            expected.add(os.path.abspath(os.path.join(dst_base, data_fn)))
        # 附件
        for a in node.get("attachments") or []:
            fn = a.get("dataFileName")
            if fn:
                expected.add(os.path.abspath(os.path.join(dst_base, fn)))
        # 子节点
        child_dst = os.path.join(dst_base, node.get("dirFileName") or "") if node.get("dirFileName") else dst_base
        child_src = os.path.join(src_base, node.get("dirFileName") or "") if node.get("dirFileName") else src_base
        for c in node.get("children") or []:
            _collect(c, child_src, child_dst)

    for root in meta.get("files", []):
        _collect(root, tree, dst_base)

    return expected

def cleanup_orphans(all_expected, state, valid_keys):
    """删除 docs-zh/ 中不在上游 meta 里的孤儿文件,并清理过期 state 条目。

    all_expected: 所有应该存在的文件绝对路径集合
    state: state 字典(会被原地修改)
    valid_keys: 当前上游 meta 中所有合法的 state key 集合
    """
    out_abs = os.path.abspath(OUT_DIR)
    removed_files = 0
    removed_dirs = 0

    # 删除孤儿文件
    for dirpath, dirnames, filenames in os.walk(OUT_DIR, topdown=False):
        for fn in filenames:
            if fn == ".translated.json":
                continue
            full = os.path.abspath(os.path.join(dirpath, fn))
            if full not in all_expected:
                os.remove(full)
                removed_files += 1
        # 删除空目录(不删 OUT_DIR 本身)
        if os.path.abspath(dirpath) != out_abs:
            try:
                if not os.listdir(dirpath):
                    os.rmdir(dirpath)
                    removed_dirs += 1
            except OSError:
                pass

    # 清理过期 state 条目(不在当前上游 meta 中的 key)
    stale_keys = [k for k in list(state.keys()) if k not in valid_keys]
    for k in stale_keys:
        del state[k]

    if removed_files:
        log(f"[清理] 删除 {removed_files} 个上游已不存在的孤儿文件,清理 {removed_dirs} 个空目录")
    if stale_keys:
        log(f"[清理] 移除 {len(stale_keys)} 个过期 state 条目")


def main():
    ap = argparse.ArgumentParser(description="Trilium 帮助文档翻译器 v4(两阶段+增量同步)")
    ap.add_argument("--init", action="store_true", help="阶段一:建骨架(翻译标题/生成ID/写属性/拷贝正文原文)")
    args = ap.parse_args()

    global GLOSSARY
    GLOSSARY = read_glossary()

    if not API_KEY and not DRY_RUN:
        log("错误:没找到 LLM_API_KEY。请到仓库 Settings → Secrets → Actions 添加。")
        sys.exit(1)

    state = load_state()
    used_ids = set()
    stats = {"translated": 0, "skipped": 0, "too_big": 0, "copied": 0, "suspect": 0}

    # ====== 第一遍:预计算 _src_base/_src_path,迁移旧版 state key ======
    # 同时收集所有合法的 state key 和期望的输出文件路径
    all_meta = []          # [(meta, tree, dst_base), ...]
    all_expected = set()   # 所有应该存在的输出文件绝对路径
    valid_keys = set()     # 当前上游 meta 中所有合法的 state key

    total_migrated = 0
    total_preserved = 0
    for tree in SRC_TREES:
        meta_path = os.path.join(tree, "!!!meta.json")
        if not os.path.exists(meta_path):
            continue
        meta = load_meta(tree)
        dst_base = os.path.join(OUT_DIR, os.path.relpath(tree, "docs"))
        for root in meta.get("files", []):
            root["_src_base"] = tree
            root["_dst_base"] = dst_base
            assign_src_paths(root, tree)
            # 收集合法 state key
            for node, _ in iter_nodes(root):
                valid_keys.add(state_key(node))
        # 收集期望的输出文件
        all_expected |= collect_expected_outputs(meta, tree, dst_base)
        all_meta.append((meta, tree, dst_base))
        m, p = migrate_state(state, meta)
        total_migrated += m
        total_preserved += p

    if total_migrated or total_preserved:
        log(f"[迁移] 旧 state key → 路径 key: hash 匹配 {total_migrated} 条, hash 失配(保留ID+标记重翻) {total_preserved} 条")

    # ====== 第二遍:执行翻译 ======
    for meta, tree, dst_base in all_meta:
        # 重新挂载 _src_base/_src_path(build_tree 递归会用到)
        for root in meta.get("files", []):
            root["_src_base"] = tree
            root["_dst_base"] = dst_base
            assign_src_paths(root, tree)

        phase = "init" if args.init else "正文翻译"
        log(f"== [{phase}] 处理树: {tree} ==")
        if args.init:
            roots = init_phase(meta, state, used_ids, stats)
        else:
            roots = translate_phase(meta, state, used_ids, stats)

        # 复刻官方 docs 目录导出形态:每棵树独立写自己的 !!!meta.json,
        # files 数组只含本树根(含完整 children 嵌套)。
        # 三个文档目录各自是完整的 Trilium 导出根,可分别打包单独导入。
        tree_out = {"formatVersion": 2, "appVersion": meta.get("appVersion") or "0.104.1", "files": roots}
        os.makedirs(dst_base, exist_ok=True)
        with open(os.path.join(dst_base, "!!!meta.json"), "w", encoding="utf-8") as f:
            json.dump(tree_out, f, ensure_ascii=False, indent=2)

    # ====== v4.0: 清理孤儿文件 + 过期 state ======
    cleanup_orphans(all_expected, state, valid_keys)

    save_state(state)

    if args.init:
        log(f"\n[init] 完成: 拷贝正文 {stats['copied']} | 标题与 ID 已写入 state")
        log("下一步: 先 review 这版骨架(树结构+中文标题+属性),确认后运行本脚本(不带 --init)翻译正文。")
    else:
        log(f"\n[translate] 完成: 翻译 {stats['translated']} | 复用 {stats['skipped']} | 太大跳过 {stats['too_big']} | 可疑 {stats['suspect']}")
        fix_missing_anchors(OUT_DIR)   # ← 修复 [缺失笔记] 锚文本(目标文件存在则回填标题)
    log(f"输出: {OUT_DIR}/ 下三个独立文档目录(各含 !!!meta.json + 正文),1:1 复刻官方 docs 结构")
    log("分别导入: 必须进入单个文档目录后再打 zip,让 !!!meta.json 落在 zip 根,例如:")
    log('  cd "docs-zh/User Guide" && zip -r "../User Guide-zh.zip" .')
    log("      注意: .translated.json 是翻译记忆缓存,在 docs-zh 根(不在任何文档目录内),不打进 zip 但要 git 提交")

if __name__ == "__main__":
    main()
