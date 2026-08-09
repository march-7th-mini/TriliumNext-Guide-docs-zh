# TriliumNext 帮助文档中文翻译

把 [TriliumNext/Trilium](https://github.com/TriliumNext/Trilium) 官方帮助文档(docs 三个目录)
翻译成简体中文,并与上游保持增量同步。翻译产物可直接导入 Trilium,内置帮助(按 `?`)自动跳转中文版。

## 仓库内容

| 文件/目录 | 说明 |
|---|---|
| `translate_trilium_Guide_docs_CHS.py` | 两阶段翻译脚本:① `--init` 建骨架(翻译标题/生成 ID/写属性),② 默认翻正文(增量,hash 对比只翻变化) |
| `.github/workflows/translate-docs-zh.yml` | 半自动工作流:手动触发 + 每周日自动检查上游更新 |
| `docs-zh/` | 翻译产物(Trilium 目录导出格式,含 `!!!meta.json`),由 workflow 生成 |
| `TRANSLATE_TUTORIAL.md` | 零基础操作教程 |

## 快速开始

1. **首次推送**:把本仓库文件推到 `main`(脚本和 workflow 必须先就位,第一次 Run workflow 才会成功)。
2. **配密钥**:仓库 → Settings → Secrets and variables → Actions → 新建 `LLM_API_KEY`(DeepSeek/OpenAI key)。
3. **手动运行**:Actions → 选本工作流 → Run workflow:
   - 勾选 **only_init**:只建骨架(树 + 中文标题 + `#originalHelpNoteId` / `#helpDoc` 属性,正文仍为英文)→ 先 review 结构;
   - 不勾选:翻译全部正文,自动开 PR。
4. **合并 PR**:review 后合并;增量同步时重新 Run workflow 即可(`.translated.json` 随结果入库,重跑只翻变化部分)。
5. **导入 Trilium**:合并后把 `docs-zh` 下载打成 zip(`!!!meta.json` 必须在 zip 根目录),Trilium → 导入。

## 设计要点

- **不 fork 上游**:workflow 用 sparse-checkout 只拉取 docs 三个目录,本仓库只有脚本和翻译结果。
- **内置帮助跳转铁律**:每个译文笔记带 `#originalHelpNoteId=_help_<源noteId>` + `#helpDoc=zh`,
  跳转补丁脚本靠这两个属性把 `?` 帮助指向中文版。
- **内部链接免改**:Trilium 导出链接是相对路径(按 `dataFileName` 解析),译文目录与英文平行,链接自动指向译文。
