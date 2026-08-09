# TriliumNext 帮助文档中文翻译

把 [TriliumNext/Trilium](https://github.com/TriliumNext/Trilium) 官方帮助文档(docs 下Developer Guide、User Guide、Release Notes这三个目录)
翻译成简体中文,并与上游保持增量同步。翻译产物可直接导入 Trilium,内置帮助(按 `?`)自动跳转中文版。

## 仓库内容

| 文件/目录 | 说明 |
|---|---|
| `translate_trilium_Guide_docs_CHS.py` | 两阶段翻译脚本:① `--init` 建骨架(翻译标题/生成 ID/写属性),② 默认翻正文(增量,hash 对比只翻变化) |
| `.github/workflows/translate-docs-zh.yml` | 半自动工作流:手动触发 + 每周日自动检查上游更新 |
| `docs-zh/` | 翻译产物,1:1 复刻官方 `docs/` 结构:三个独立文档目录(User/Developer/Release Notes),每个目录各含自己的 `!!!meta.json`(files 含本树根 + 完整 children 嵌套),可分别打包导入。由 workflow 生成 |

## 快速开始

1. 把 `docs-zh` 下载打成 zip(`!!!meta.json` 必须在 zip 根目录),Trilium → 导入。
2. 需要配合前端脚本插件：TriliumNext中文版帮助文档跳转补丁.zip（标签 #run=frontendStartup）
3. ⚠ 不要把整个 `docs-zh/` 打成一个 zip——根目录没有 `!!!meta.json`,导入器不认。
   

## 设计要点

- **内置帮助跳转铁律**:每个译文笔记带 `#originalHelpNoteId=_help_<源noteId>` + `#helpDoc=zh`,
  跳转补丁脚本靠这两个属性把 `?` 帮助指向中文版。
- **内部链接免改**:Trilium 导出链接是相对路径(按 `dataFileName` 解析),译文目录与英文平行,链接自动指向译文。
