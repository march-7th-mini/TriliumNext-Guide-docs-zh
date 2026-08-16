#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trilium 目录导出格式翻译器 v3(两阶段)
=======================================
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
  python3 translate_trilium_v2.py --init            # 初始化(可反复跑,增量)
  python3 translate_trilium_v2.py                   # 翻译正文(可反复跑,增量)
  python3 translate_trilium_v2.py --init --dry-run  # 试跑:不调 API

说明:
  - 内部链接是相对路径 <a class="reference-link" href="...">,只依赖 dataFileName;
    译文目录平行,链接自动指向译文对应文件,无需改写。
  - 内置帮助 ID 铁律:内置帮助 noteId = "_help_" + GitHub docs 树对应笔记 noteId,
    故 originalHelpNoteId 必须写成 "_help_<源noteId>",跳转补丁脚本才能搜到。
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
        "3. 完整保留 HTML 标签,尤其是 <a class=\"reference-link\" href=\"...\"> 的 href 值一字不改\n"
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
    """节点的 state 键:有正文文件用文件相对路径,无正文(book 容器)用 meta:noteId。"""
    if node.get("dataFileName"):
        return node["dataFileName"]
    return "meta:" + node.get("noteId", "")


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
            done = rec.get("status") == "done" and rec.get("hash") == cur_hash
            if not os.path.exists(dst_path):
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
    return out


def _translate_body_file(src_path, dst_path, state, key, cur_hash, stats):
    """翻译单个正文文件。"""
    with open(src_path, encoding="utf-8", errors="replace") as f:
        content = f.read()

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
            time.sleep(0.5)
        stats["translated"] += 1

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(translated)
    rec = state.get(key, {}) or {}
    rec["hash"] = cur_hash
    rec["status"] = "done"
    state[key] = rec


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


def main():
    ap = argparse.ArgumentParser(description="Trilium 帮助文档翻译器 v3(两阶段)")
    ap.add_argument("--init", action="store_true", help="阶段一:建骨架(翻译标题/生成ID/写属性/拷贝正文原文)")
    args = ap.parse_args()

    global GLOSSARY
    GLOSSARY = read_glossary()

    if not API_KEY and not DRY_RUN:
        log("错误:没找到 LLM_API_KEY。请到仓库 Settings → Secrets → Actions 添加。")
        sys.exit(1)

    state = load_state()
    used_ids = set()
    stats = {"translated": 0, "skipped": 0, "too_big": 0, "copied": 0}

    for tree in SRC_TREES:
        meta_path = os.path.join(tree, "!!!meta.json")
        if not os.path.exists(meta_path):
            log(f"[跳过] 没找到 {meta_path}")
            continue
        meta = load_meta(tree)
        dst_base = os.path.join(OUT_DIR, os.path.relpath(tree, "docs"))

        # 给每个根挂上基础路径,供 build_tree 递归使用
        for root in meta.get("files", []):
            root["_src_base"] = tree
            root["_dst_base"] = dst_base

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

    save_state(state)

    if args.init:
        log(f"\n[init] 完成: 拷贝正文 {stats['copied']} | 标题与 ID 已写入 state")
        log("下一步: 先 review 这版骨架(树结构+中文标题+属性),确认后运行本脚本(不带 --init)翻译正文。")
    else:
        log(f"\n[translate] 完成: 翻译 {stats['translated']} | 复用 {stats['skipped']} | 太大跳过 {stats['too_big']}")
    log(f"输出: {OUT_DIR}/ 下三个独立文档目录(各含 !!!meta.json + 正文),1:1 复刻官方 docs 结构")
    log("分别导入: 必须进入单个文档目录后再打 zip,让 !!!meta.json 落在 zip 根,例如:")
    log('  cd "docs-zh/User Guide" && zip -r "../User Guide-zh.zip" .')
    log("      注意: .translated.json 是翻译记忆缓存,在 docs-zh 根(不在任何文档目录内),不打进 zip 但要 git 提交")


if __name__ == "__main__":
    main()
