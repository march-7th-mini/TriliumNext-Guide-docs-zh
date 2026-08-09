# 故障排除
## Trilium 仅显示空白窗口

Trilium 使用基于 Chromium（Google Chrome 的开源替代品）的 Electron；为了提高性能，它利用了 _GPU 加速_。在某些情况下，GPU 不兼容（尤其是在较旧的集成显卡型号上）可能导致无法渲染任何内容，从而出现空白窗口。

要解决此问题，请尝试使用以下命令行参数运行 Trilium：

```
trilium --disable-gpu
```

如果这不起作用，也请尝试以下命令：

*   `trilium --disable-gpu-compositing`
*   `ELECTRON_OZONE_PLATFORM_HINT=x11 trilium`（此命令在 Wayland 上强制使用 X11 渲染）

如果在此之后 Trilium 能正常渲染，Trilium 提供了一个内置选项来禁用 GPU 加速：转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _外观_，找到 _性能_ 部分，然后取消勾选 _硬件加速 (GPU)_。