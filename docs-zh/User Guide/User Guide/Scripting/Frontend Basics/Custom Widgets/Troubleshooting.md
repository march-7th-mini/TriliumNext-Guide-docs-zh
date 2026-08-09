# 故障排查
## 为什么我的小组件会被其他 UI 元素裁剪

出于性能和布局的考虑，Trilium 中小组件的尺寸与其子元素无关。在 CSS 层面，这意味着小组件容器应用了 `contain: size`。

如果小组件具有固定尺寸（或基于其父容器），这可以正常工作，但若要使小组件根据其内容调整大小，请应用以下更改：

```diff
class MyWidget extends api.RightPanelWidget {

+   constructor() {
+       super();
+       this.contentSized();
+   }
        
}
```

或者，在其 CSS 中应用 `contain: none`。