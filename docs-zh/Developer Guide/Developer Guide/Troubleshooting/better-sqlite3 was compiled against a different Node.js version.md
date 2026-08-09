# better-sqlite3 是针对不同版本的 Node.js 编译的
这通常发生在运行 `desktop` 或 `server` 的开发版本时，但这种情况不应像以前那样频繁发生。原因是 `better-sqlite3` 是一个原生依赖，它针对系统的 Node.js（如 `server` 所使用的）或 Electron 的 Node.js（如 `desktop` 所使用的）有不同的构建版本。

要解决此问题，请前往 `apps/server` 并运行 `pnpm rebuild`。对于 Electron（`desktop`），通常不需要此步骤，但 `pnpm postinstall` 应该可以解决。

如果您能持续复现此问题，请提交错误报告。