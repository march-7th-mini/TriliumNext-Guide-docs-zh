# 系统要求
*   使用 Docker 时，服务器可以在 Windows、Linux 和 macOS 设备上运行。
*   为 Linux x64 和 ARM（`aarch64`）架构提供了原生二进制文件。

## 旧版 ARM 支持

Docker 构建也提供 `linux/arm/v7` 和 `linux/arm/v8` 平台。这些平台被视为旧版，因为 Trilium 使用的 Node.js 版本 24 已[官方降级](https://github.com/nodejs/node/commit/6682861d6f)了对这些平台的支持至“实验性”级别。

因此，Trilium 需要为这些版本使用 Node.js 22。一旦 Node.js 22 不再兼容，对 `armv7` 和 `armv8` 的支持将被完全移除。

无论上游支持情况如何，这些平台都是基于尽力而为的原则提供支持，并非由 Trilium 开发团队官方支持。我们接受错误报告，但不会优先处理；欢迎贡献代码。