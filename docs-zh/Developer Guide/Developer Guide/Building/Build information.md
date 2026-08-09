# 构建信息
*   提供关于构建时间及对应 Git 修订版本的信息。
*   当打开“关于”对话框时，这些信息会显示给客户端。
*   构建信息被硬编码在 `apps/server/src/services/build.ts` 文件中。该文件通过 `chore:update-build-info` 自动生成，而此命令本身会在 CI 中进行构建时自动运行。