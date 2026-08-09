# 导出静态 HTML 用于网络发布

如 <a class="reference-link" href="../Sharing.md">分享</a> 中所述，Trilium 可以充当公共服务器，其中共享笔记以只读模式显示。虽然这在大多数情况下可行，但它通常不适用于高流量网站，并且由于运行在 Node.js 服务器上，存在被利用的潜在风险。

另一种替代方案是生成静态 HTML 文件（就像 [MkDocs](https://www.mkdocs.org/) 等其他静态站点生成器一样）。由于普通的 HTML ZIP 导出不包含任何样式或附加功能，Trilium 提供了一种将 <a class="reference-link" href="../Sharing.md">分享</a> 功能的相同布局和样式导出为静态 HTML 文件的方法。

除了增强安全性之外，这些 HTML 文件还易于部署在“无服务器”平台上，例如 GitHub Pages 或 CloudFlare Pages，并且非常容易缓存。

> [!TIP]
> Trilium 的文档（可在 [docs.triliumnotes.org](https://docs.triliumnotes.org/) 获取）就是使用此功能构建的，即导出为静态 HTML 文件，然后自动部署到 CloudFlare Pages。
> 
> 该过程是[自动化的](https://github.com/TriliumNext/Trilium/blob/main/apps/edit-docs/src/build-docs.ts)，通过导入 Markdown 文档并通过脚本将其导出为静态网页格式来实现。

## 与普通分享的区别

除了普通的 <a class="reference-link" href="../Sharing.md">分享</a> 之外，导出为静态 HTML 文件还有一些细微差别：

*   URL 结构不同。普通分享的 URL 类似于 `example.com/share/noteid`，而导出的笔记遵循层级结构，例如 `docs.triliumnotes.org/user-guide/concepts/navigation/tree-concepts`。
*   `favicon.ico` 不会自动处理，需要在导出生成后在服务器上手动添加。
*   笔记的“最后更新”时间不可用。
*   搜索功能的工作方式略有不同，因为普通搜索需要活跃的 API 才能工作。在静态导出中，搜索仍然有效，但使用了不同的机制，因此结果可能会有所不同。

## 与普通 .zip 导出的区别

*   文件/URL 的名称将优先使用 `shareAlias` 以获得简洁的 URL。
*   导出需要一个可用的 Web 服务器，因为如果通过 Web 浏览器本地访问，由于使用了模块脚本，页面将无法正常渲染。
*   目录结构也略有不同：
    *   普通的 HTML 导出会生成一个索引文件和一个单独的目录。
    *   相反，对于静态导出，顶层根目录成为索引文件，子目录则直接位于根目录下。
    *   这使得可以轻松地发布到网站，而无需强制除根笔记之外的所有内容都位于子目录中。

## 本地测试

如前所述，导出的静态页面需要网站才能正常运行。为了在本地测试，需要使用 Web 服务器。

一个示例是使用基于 Node.js 的 [`http-server`](https://www.npmjs.com/package/http-server)，可以通过以下方式安装：

```
npm i -g http-server
```

安装完成后，只需：

1.  解压导出的 .zip 文件。
2.  在解压后的目录内，运行 `http-server`。
3.  访问提示的地址（例如 [http://localhost:8080](http://localhost:8080)）。

## 自动化

<a class="reference-link" href="../ETAPI%20(REST%20API).md">ETAPI (REST API)</a> 可能可用于在计划任务上自动化导出。