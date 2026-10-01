# 构建信息
*   提供关于构建时间及对应 Git 修订版本的上下文信息。
*   当客户端进入关于对话框时，会向其显示这些信息。
*   构建信息硬编码在 `packages/trilium-core/src/services/build.ts` 中。该文件通过 `chore:update-build-info` 自动生成，而该命令本身在 CI 中进行构建时会自动运行。
*   传入 `--from-commit` 会以提交的日期代替当前时间进行标记，从而使同一源代码的两次构建结果一致。Flathub 构建使用了该选项，因为它会重新构建已发布的标签。