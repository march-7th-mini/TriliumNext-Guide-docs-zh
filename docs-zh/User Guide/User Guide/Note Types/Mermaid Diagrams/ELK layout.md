# ELK 布局

Mermaid 支持一种不同的布局引擎，能够处理稍微复杂一些的图表，称为 [Eclipse 布局内核（ELK）](https://eclipse.dev/elk/)。Trilium 也支持这些，但默认并未启用。

要为任何图表激活 ELK，请在图表的最开始处插入以下 YAML 前置元数据：

```yaml
---
config:
  layout: elk
---
```

| 关闭 ELK | 开启 ELK |
| --- | --- |
| ![](ELK%20layout_ELK%20off.svg) | ![](ELK%20layout_ELK%20on.svg) |