# 发布新版本
发布主要由 CI 处理：

*   GitHub 上的版本会自动发布，包括取自文档的变更日志描述。
*   会在 Winget 仓库中自动创建一个 PR，以更新到新版本。

发布通常直接从 `main` 分支进行。对于热修复，流程相同，但使用不同的分支，更多信息请参阅 <a class="reference-link" href="../Branching%20strategy.md">分支策略</a>。

流程如下：

1.  编辑 <a class="reference-link" href="../Documentation.md">文档</a>，在 _发布说明_ 部分添加相应条目。
2.  在根目录的 `package.json` 中，将 `version` 设置为要发布的新版本。
3.  运行 `chore:update-version` 以自动更新其余 `package.json` 文件的版本。
4.  同时运行 `pnpm i` 以更新包锁文件。
5.  提交对 `package.json` 文件和 `package-lock.json` 的更改。提交信息通常为 `chore(release): prepare for v1.2.3`。
6.  为新创建的提交打标签：`git tag v1.2.3`
7.  推送提交和新创建的标签：`git push; git push --tags`。
8.  等待 CI 完成。
9.  当版本在 GitHub 中自动创建后，下载它以确保其正常工作。