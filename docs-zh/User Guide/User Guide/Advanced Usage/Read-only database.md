# 只读数据库
> [!WARNING]
> 此功能仍处于预览阶段，可能会遇到问题，甚至该功能可能会完全消失。
> 如有任何问题，欢迎[报告](../Troubleshooting/Reporting%20issues.md)。

只读数据库是<a class="reference-link" href="Sharing.md">分享</a>笔记的一种替代方案。虽然分享功能在将页面以维基、博客类似格式发布到互联网上时效果很好，但它无法提供 Trilium 背后的全部功能，例如高级<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>、<a class="reference-link" href="../Collections.md">集合</a>背后的交互性，或各种<a class="reference-link" href="../Note%20Types.md">笔记类型</a>。

当数据库处于只读模式时，Trilium 应用程序可以正常使用，但编辑功能被禁用，更改仅在内存中进行。

## 功能说明

*   所有笔记均为只读，无法进行编辑。
*   通常会更改数据库的功能（如最近笔记列表）将被禁用。

## 限制

*   某些功能可能会“漏网”并最终创建笔记，例如。
    *   但是，数据库仍然是只读的，因此如果服务器重启，所有修改都将被重置。
    *   每当发生这种情况时，日志中将显示 `ERROR: read-only DB ignored`。

## 将数据库设置为只读

首先，确保数据库已初始化（例如，首次设置已完成）。然后修改 [config.ini](Configuration%20\(config.ini%20or%20environment%20variables\).md)，找到 `[General]` 部分并添加一个新的 `readOnly` 字段：

```
[General]
readOnly=true
```

如果您的服务器已在运行，请重启以应用更改。

同样，要禁用只读模式，请删除该行或将其设置为 `false`。