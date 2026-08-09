# 直接提供笔记内容
访问共享笔记时，Trilium 会将其渲染为网页。有时需要直接提供内容，以便脚本使用或用户下载。

| 以网页（HTML）形式显示的笔记 | 以原始格式显示的笔记 |
| --- | --- |
| <figure class="image"><img style="aspect-ratio:738/275;" src="1_Serving directly the content of a note_image.png" width="738" height="275"></figure> | ![](Serving%20directly%20the%20content%20of%20a%20note_image.png) |

## 通过向笔记添加属性

只需添加 `#shareRaw` 属性，当从分享 URL 访问时，该笔记将始终以 _原始_ 格式渲染。

## 通过修改 URL

在 URL 后附加 `?raw` 即可显示笔记的原始格式，无论笔记上是否添加了 `#shareRaw` 属性。

![](Serving%20directly%20the%20content%20of%20a%20note_image.png)