#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 Trilium Weblate 提取简体中文术语,生成 glossary.tsv(英文<TAB>中文)。

数据源: https://hosted.weblate.org 的 trilium 项目
  - client 组件(界面字符串,3369 单元)
  - server 组件(433 单元)
这些是程序界面术语,与帮助文档共用同一套词汇,可作为翻译一致性基准。

用法:
  python3 build_glossary.py          # 拉取并生成 glossary.tsv
  python3 build_glossary.py --dry    # 只打印统计和样例,不写文件
"""
import json
import re
import sys
import time
import urllib.request

WEBLATE = "https://hosted.weblate.org"
PROJECT = "trilium"
COMPONENTS = ["client", "server"]   # 界面字符串是术语最佳来源
LANG = "zh_Hans"
OUT = "glossary.tsv"

MAX_SRC_LEN = 40      # 英文源串最大长度
MAX_WORDS = 4         # 英文最多单词数(短术语;长句过滤掉)

PLACEHOLDER = re.compile(r"\{\{|\}|%s|%d|%1\$|&lt;|&gt;|<[A-Za-z/]+>", re.I)
BAD_CHARS = re.compile(r"[:：。.!?！？\n\r\t;,，()（）]")

# ---- 术语白名单(Trilium 领域/技术词;大小写不敏感,存小写) ----
TERM = set("""
trilium note notes attribute attributes label labels relation relations script scripts
widget widgets snippet snippets launcher launchers hoist hoisted hoisting clone cloned
template templates attachment attachments book books calendar kanban mermaid excalidraw
mindmap relationmap search savedsearch shortcut shortcuts sync syncing backup backups
export import archive archived trash readonly read-only protected code render webview
web-view dashboard ontology namespace icon icons editor tree sidebar toolbar frontend
backend server client mobile desktop database db sql css html js markdown regex regexp
certificate proxy auth authentication oauth api rest websocket http https ssh cli gui
json xml yaml pdf url uri uuid id ui ux admonition anchor anchors backlink backlinks
breadcrumb breadcrumbs checklist checkbox dropdown floating pinned boolean integer string
array object function variable javascript typescript node nodejs npm pnpm git github
docker linux windows macos android ios browser binary textarea datatype datafolder
datadir appdata port portforwarding c4 opml mfa picture-in-picture openai-compatible
""".split())

# ---- 功能词黑名单(冠词/介词/代词/be/助动词/连词 + 常见 UI 动词/量词) ----
BLACK = set("""
the a an and or of to for in on at by with from is are was were be been being have has had
do does did not no yes but if then than as so this that these those it its you your yours we
our us they their them he she his her i me my all any some more most just also very other
another such what when where which why who whom how there here now each every both few many
much back down up off out over under into onto about after before during against between
without within through above below along among around behind besides beyond despite except
like near past since till until per via ok okay new old add added adding edit edited editing
delete deleted deleting remove removed removing create created creating update updated
updating open opened close closed save saved saving cancel cancelled canceling done apply
applied default options option settings setting show shown hide hidden enable enabled
disable disabled use used using set sets auto-save auto-detected xy
""".split())


def _is_term_token(t):
    """单个英文词是否算术语:命中白名单 / 带连字符的复合词 / 全大写缩写。"""
    return t.lower() in TERM or "-" in t or (t.isupper() and len(t) >= 2)


def _is_black_token(t):
    return t.lower() in BLACK


def parse_po(text):
    """手写 PO 解析器:提取 (msgid, msgstr) 对,支持多行拼接与转义。"""
    entries = []
    msgid = None
    msgstr = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("#") or not line:
            continue
        if line.startswith("msgid "):
            if msgid is not None and msgstr is not None:
                entries.append((msgid, msgstr))
            msgid = _po_str(line[len("msgid "):])
            msgstr = ""
        elif line.startswith("msgstr "):
            msgstr = _po_str(line[len("msgstr "):])
        elif line.startswith('"') and msgid is not None:
            part = _po_str(line)
            if msgstr is None:
                msgid += part
            else:
                msgstr += part
    if msgid is not None and msgstr is not None:
        entries.append((msgid, msgstr))
    return entries


def _po_str(s):
    """解析 PO 字符串字面量(去引号、处理转义)。"""
    s = s.strip()
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    return s.replace(r"\n", "\n").replace(r"\"", '"').replace(r"\\", "\\")


def fetch_units(component):
    """拉取某组件的 zh_Hans 翻译(下载 PO 导出,1 个请求/组件)。
    PO 的 msgid 是真实英文显示文本(JSON 导出是 i18n 键名,不能用)。"""
    url = f"{WEBLATE}/download/{PROJECT}/{component}/{LANG}/?format=po"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                text = r.read().decode("utf-8")
            return [{"source": e[0], "target": e[1]} for e in parse_po(text)]
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 20 * (attempt + 1)
                print(f"[限流] 等待 {wait}s 后重试 {component} ...", file=sys.stderr)
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"{component}: 连续 3 次 429,放弃")


def clean(s):
    if isinstance(s, list):
        s = " ".join(x for x in s if x)
    return (s or "").strip()


def is_term(src, tgt):
    """判定是否值得进术语表:Trilium/技术术语,无占位符,确已翻译。
    只保留专业术语,过滤常见词(Back/Cancel/April/Add Column 等)。"""
    if not src or not tgt:
        return False
    if src.lower() == tgt.lower():          # 没翻译的
        return False
    if PLACEHOLDER.search(src) or PLACEHOLDER.search(tgt):
        return False
    if BAD_CHARS.search(src) or BAD_CHARS.search(tgt):
        return False
    if len(src) > MAX_SRC_LEN or len(tgt) > MAX_SRC_LEN * 2:
        return False
    if "your-" in src.lower():            # 示例占位符(如 your-etapi-token)
        return False
    toks = src.split()
    if len(toks) > MAX_WORDS:
        return False
    terms = sum(1 for t in toks if _is_term_token(t))
    has_black = any(_is_black_token(t) for t in toks)
    n = len(toks)
    if n == 1:
        return _is_term_token(toks[0]) and not _is_black_token(toks[0])
    if n == 2:
        return terms >= 1 and not has_black
    return terms >= 2 and not has_black


def main():
    seen = {}
    for comp in COMPONENTS:
        print(f"[拉取] {comp} ...", file=sys.stderr)
        try:
            units = fetch_units(comp)
        except Exception as e:
            print(f"[失败] {comp}: {e}", file=sys.stderr)
            continue
        kept = 0
        for u in units:
            src = clean(u.get("source"))
            tgt = clean(u.get("target"))
            if is_term(src, tgt):
                key = src.lower()
                if key not in seen:         # client 优先,server 补缺
                    seen[key] = (src, tgt)
                    kept += 1
        print(f"[统计] {comp}: 共 {len(units)} 单元,筛出 {kept} 条", file=sys.stderr)

    pairs = sorted(seen.values(), key=lambda x: x[0].lower())
    lines = [f"{s}\t{t}" for s, t in pairs]

    if "--dry" in sys.argv:
        print(f"共 {len(lines)} 条术语(不写文件),样例:")
        for l in lines[:30]:
            print("  " + l)
        return

    # 失败保护:只有成功拉到数据才覆盖旧文件
    if not lines:
        print("[警告] 没有拉到任何术语,保留现有 glossary.tsv 不变", file=sys.stderr)
        sys.exit(1)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"已写入 {OUT}: {len(lines)} 条")


if __name__ == "__main__":
    main()
