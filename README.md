<div align="left">

# TriliumNext 内置帮助说明文档（简中版）

**简体中文 · [English](./README_EN.md)**

> 将 TriliumNext 官方帮助文档 **User Guide / Developer Guide / Release Notes** 全量翻译为简体中文，
> 产物可直接导入 Trilium，点击内置帮助（`?`）自动跳转中文版，并与上游保持每周自动增量同步。

[![Workflow 状态](https://github.com/march-7th-mini/TriliumNext-Guide-docs-zh/actions/workflows/translate-docs-zh.yml/badge.svg)](https://github.com/march-7th-mini/TriliumNext-Guide-docs-zh/actions/workflows/translate-docs-zh.yml)

</div>

---

## 这是什么

本项目将 [TriliumNext/Trilium](https://github.com/TriliumNext/Trilium) 官方帮助文档（`docs/` 下的 **Developer Guide**、**User Guide**、**Release Notes** 三个文档）翻译为简体中文。

翻译产物 1:1 复刻官方目录结构，以 Trilium 导出格式存放在 `docs-zh/` 下，可直接打包导入 Trilium。配合前端跳转补丁，界面上的 `?` 帮助按钮会自动打开中文版文档。

> 相关讨论：[TriliumNext 官方社区 · 中文帮助文档建议帖](https://github.com/orgs/TriliumNext/discussions/10768)

## 特性

| 特性 | 说明 |
| --- | --- |
| 全量翻译 | 三个文档全量简体中文，1:1 复刻官方目录结构，完美保留内链笔记，可分别导入 |
| 内置帮助跳转 | 每篇译文带 `#originalHelpNoteId=_help_<源noteId>` + `#helpDoc=zh`，与英文版一一对应，跳转补丁靠这两个标签定位中文版 |
| 跳转补丁 | 帮助分屏与快速编辑弹窗自动切换中文；无中文版时保留英文（无闪屏） |
| 增量同步 | 每周自动检查上游更新，已译内容按源 hash + 译文 hash 双重校验增量复用，只翻译变化的部分 |

## 效果演示

点击界面 `?` 帮助按钮，自动打开对应中文文档：

| 拆分面板 · 跳转中文帮助 | 快速编辑面板 · 跳转帮助 |
| --- | --- |
| ![拆分面板](https://github.com/user-attachments/assets/8df01508-7d28-4089-b5b6-7cdf4b1f7f6b) | ![快速编辑面板](https://github.com/user-attachments/assets/e6c81185-7f5e-4897-b0f5-be3e3d3c86fa) |

## 使用方法

> 📥 **附件下载**：三个文档 zip 与跳转补丁 zip 均发布在仓库 **Releases 页面**（仓库主页右侧 **Releases** 入口），请下载最新版附件。Release 附件会随翻译更新重新发布，定期更新即可。

### 1. 导入翻译文档

到 **Releases** 下载 `User-Guide.zip`（或三个文档 zip 全部下载）。然后：Trilium → 左侧目录树任意位置右键 → **导入**，选择刚下载的 zip。

> ⚠️ 每个 zip 中的 `!!!meta.json` 必须在 **zip 根目录**。自己打包时请进入单个文档子目录后再压缩（例如进入 `docs-zh/User Guide` 后打包其中全部内容）；**不要**把整个 `docs-zh/` 打成一个包——它的根目录没有 `!!!meta.json`，导入器不认。

![导入](https://github.com/user-attachments/assets/4c0a48d3-8827-44f8-95fe-ffe5ceb06160)

### 2. 导入跳转补丁

到 **Releases** 下载 `TriliumNext中文版帮助文档跳转补丁.zip`，导入时**务必取消勾选「安全导入」**。导入后会生成一个 JS 前端笔记（带 `#run=frontendStartup` 标签），**刷新页面后自动生效**。

> **必须安装此补丁**，才能实现内置帮助（`?`）自动跳转中文版。若某篇文档暂无中文版，会自动回退到内置英文文档。

### 3. 验证效果

- 点击界面右上角 `?` 按钮 → 帮助分屏直接显示中文文档
- 在快速编辑弹窗（右键笔记 → 打开帮助）中打开帮助链接 → 同样跳转中文版

<details>
<summary><b>展开可以了解更多细节</b></summary>

## 仓库内容

| 文件 / 目录 | 说明 |
| --- | --- |
| <nobr>translate_trilium_Guide_docs_CHS.py</nobr> | 两阶段翻译脚本：① `--init` 建骨架（翻译标题 / 生成 ID / 写属性），② 默认翻正文（增量，hash 对比只翻变化） |
| <nobr>.github/workflows/translate-docs-zh.yml</nobr> | 半自动工作流：手动触发 + 每周日自动检查上游更新，自动开 PR |
| <nobr>docs-zh/</nobr> | 翻译产物，1:1 复刻官方 `docs/` 结构：三个独立文档目录（User / Developer / Release Notes），每个目录各含自己的 `!!!meta.json`，可分别打包导入。由 workflow 生成 |
| <nobr>build_glossary.py</nobr> | 术语表构建脚本：从 Trilium 官方 Weblate（hosted.weblate.org 的 trilium 项目 client / server 组件）抓取词条，生成 `glossary.tsv`。用法：`python3 build_glossary.py`（`--dry` 只抓取不写文件） |
| <nobr>glossary.tsv</nobr> | 术语表（TAB 分隔：英文 → 中文）。翻译脚本启动时自动加载，向 prompt 注入前 60 条术语，保证术语全文一致 |
| <nobr>TriliumNext中文版帮助文档跳转补丁.zip</nobr> | 前端跳转补丁（JS 笔记，`#run=frontendStartup`），随 Release 发布 |
| <nobr>.gitignore</nobr> | 忽略 Python 缓存等杂项文件 |

## 更新机制

本仓库配置了 GitHub 工作流：**每周日自动检查上游更新**（也可在 Actions 页手动触发）。

```
上游 docs → sparse-checkout 只拉取三个目录 → hash 对比 → 只翻译有变化的文件 → 译文完整性校验 → 自动开 PR
```

- 已翻译内容按 hash **增量复用**，增量更新成本极低
- 可关注仓库的 PR 日志了解翻译进度
- ⚠️ Release 中的 zip 附件可能落后于仓库实际翻译进度，建议定期下载最新附件重新导入

## 工作原理

### 内置帮助跳转「铁律」

Trilium 内置英文帮助的笔记 ID = `_help_` + GitHub 文档树对应笔记的 noteId（如 `_help_BOCnjTMBCoxW`）。

翻译脚本为每篇译文追加两个标签：

- `#originalHelpNoteId=_help_<源noteId>` —— 标记对应哪篇英文帮助
- `#helpDoc=zh` —— 标记为中文帮助

跳转补丁靠这两个标签，把 `?` 打开的英文帮助定位到中文版。

### 内部链接免改

Trilium 导出链接是相对路径（按 `dataFileName` 解析）。译文目录与英文目录平行，链接自动指向译文对应文件，**无需改写任何链接**。

### 两阶段翻译

1. **初始化（`--init`）**：建树 + 批量翻译标题 + 生成稳定新 ID（`_zh_xxx`）+ 写属性。正文仍是英文原文，先 review 骨架结构。
2. **正文翻译**：增量翻译正文，已翻译的按 hash 跳过，可断点续跑。每次翻译成功后额外记录译文文件哈希（`output_hash`），下次运行时对比磁盘译文，防止 state 与实际译文不一致。

> 为什么先骨架后正文？标题和 ID 先定好并持久化，正文里的内部链接才能稳定指向中文笔记；骨架 PR 也方便先 review 结构再翻正文。

### 跳转补丁（V3）原理

```
打开英文 _help_* 笔记（两种入口）
  · ? ：contextual-help 帮助分屏
  · 右键 / Ctrl+点击：快速编辑弹窗（_popup-editor）
        ↓
猴子补丁 NoteContext.setNote（加载英文前拦截）
        ↓
按 #originalHelpNoteId 查找中文版
        ↓
有中文版 → 改用中文 noteId 打开（无闪屏）
        ↓
没有中文版 → 照常打开英文原版
```

补丁为纯前端 JS，**无需后端脚本权限，不向外部发送任何数据**。

## 常见问题

| 问题 | 原因 & 解决 |
| --- | --- |
| 导入 Trilium 失败 | 99% 是 zip 结构不对：`!!!meta.json` 必须在 zip 根目录。进入单个文档子目录后打包，不能把整个 `docs-zh` 打成包 |
| 点 `?` 还是英文 | 补丁未生效：确认脚本笔记带 `#run=frontendStartup` 标签并已刷新页面；或该篇文档暂无中文版（会自动回退英文） |
| 想停用中文帮助 | 临时：删掉脚本笔记的 `#run=frontendStartup` 标签后刷新；永久：删除脚本笔记和所有中文帮助笔记 |

## 如何修改此仓库用于翻译其他语种

想把文档翻译成其它语言（或换用其它翻译模型）？核心只需改 `translate_trilium_Guide_docs_CHS.py` 里几处关键位置：

### 1. 翻译目标语言（必须）

脚本中的翻译指令：

```python
prompt = (
    "你是一位专业的技术文档翻译。请把下面的英文 Markdown 文档翻译成简体中文。
"
    ...
)
```

把「简体中文」改成目标语言（如 `日本語`、`한국어`、`Deutsch`）。同一 prompt 里的其它要求建议一并保留：保留 Markdown 结构、HTML 的 `href` 一字不改、代码块不翻译、专有名词保留英文。

### 2. 语言标签（必须）

脚本为每篇译文写入的 `helpDoc` 标签值就是语言代码，跳转补丁靠它识别语言：

```python
attrs.append({"type": "label", "name": "helpDoc",
              "value": "zh", "isInheritable": False, "position": max_pos + 20})
```

把 `"zh"` 改成目标语言代码（如 `"ja"`、`"ko"`、`"de"`），并同步修改跳转补丁脚本里查找的语言代码，否则跳转不会命中。

### 3. 输出目录（可选）

```python
OUT_DIR = "docs-zh"   # 改成如 "docs-ja"，避免与现有翻译混在一起
```

### 4. 换用其它翻译模型（可选）

```python
MODEL = "deepseek-chat"                      # 如 "gpt-4o-mini"
BASE_URL = "https://api.deepseek.com"        # 如 "https://api.openai.com/v1"
```

### 5. 术语表（建议同步）

翻译脚本启动时会自动加载 `glossary.tsv`（TAB 分隔：源语言 → 目标语言），向 prompt 注入前 60 条术语，保证术语全文一致（`GLOSSARY_FILE` / `GLOSSARY_INJECT` 在脚本顶部，文件不存在则自动跳过）：

```python
GLOSSARY_FILE = "glossary.tsv"   # Weblate 术语表（可选，不存在则跳过）
GLOSSARY_INJECT = 60             # prompt 中最多注入的术语条数
```

`glossary.tsv` 由术语表构建脚本从官方 Weblate 抓取生成，改语种时同步修改其语言配置并重新生成：

```python
# build_glossary.py
LANG = "zh_Hans"      # 改成目标语言的 Weblate 语言代码，如 "ja"、"ko"、"de"
PROJECT = "trilium"   # Weblate 项目名（默认 trilium，一般不用改）
```

```bash
python3 build_glossary.py     # 重新生成 glossary.tsv（--dry 只抓取不写文件）
```

> 若目标语言在 Weblate 没有术语，删除 `glossary.tsv` 即可，翻译脚本会自动跳过，不影响翻译。

### 6. 跳转补丁（视情况）

补丁 zip 内的 JS 按 `#originalHelpNoteId` 标签查找译文，**本身与语言无关**——只要译文带该标签，单语种场景无需修改即可复用。

仅当**多语种并存**（同一文档同时存在中文版、日文版等）时，`api.searchForNotes` 可能返回多条结果，补丁默认取第一条，可能跳错版本。此时需要在补丁 JS 的查询里追加语言过滤：

```js
// TriliumNext中文版帮助文档跳转补丁.js → findChinese()
const query = '#originalHelpNoteId = "' + englishNoteId.replace(/"/g, '\\"') + '"' +
              ' AND #helpDoc = "目标语言代码"';   // 如 "ja"
```

改完重新打包 zip 导入即可。

### 配套问题

| 问题 | 原因 & 解决 |
| --- | --- |
| Actions 报错「没找到 LLM_API_KEY」 | 在仓库 Settings → Secrets and variables → Actions 添加 `LLM_API_KEY`（DeepSeek / OpenAI 的 `sk-` key），workflow 会自动注入给脚本 |
| 翻译到一半失败 / 超时 | 重新 Run workflow 即可，脚本有记忆（`.translated.json`），已翻译的会自动跳过（增量续跑） |
| 不想每周日自动跑 | 删掉 workflow 中 `schedule:` 那几行，只保留手动触发 |
| 为什么不用 fork 官方仓库 | fork 会复制几千个源码文件；workflow 用 sparse-checkout 只拉取 docs 三个目录，本仓库只存脚本与翻译结果。改语种同理，改完脚本即可 |



</details>

## 关于翻译

- 翻译主要由 DeepSeek + 术语表约束完成。首次为全量初始化，文本量较大，尚未人工逐一校对；如有词不达意之处，欢迎反馈或提交 PR 共同维护。
- 本仓库基于 TriliumNext/Trilium `main` 分支，与官方保持同步。

## 致谢

特别感谢 [TriliumNext](https://github.com/TriliumNext/Trilium) 团队。

如果这个项目对你有帮助，欢迎 ⭐ Star、分享，或提交 Issue / PR 一起完善中文文档！

---

**相关链接**：[官方社区建议帖](https://github.com/orgs/TriliumNext/discussions/10768) · [TriliumNext/Trilium](https://github.com/TriliumNext/Trilium)
