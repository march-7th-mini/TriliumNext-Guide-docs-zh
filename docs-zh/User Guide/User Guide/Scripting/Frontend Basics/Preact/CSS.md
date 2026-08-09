# CSS
## 内联样式

```jsx
<div style={{
    display: "flex",
    height: "53px",
    width: "fit-content",
    fontSize: "0.75em",
    alignItems: "center",
    flexShrink: 0            
}}>/* [...] */</div>
```

## 自定义 CSS 文件

只需创建一个<a class="reference-link" href="../../../Theme%20development/Custom%20app-wide%20CSS.md">自定义应用级 CSS</a>。确保类名具有足够的唯一性，以免与其他 UI 元素冲突，建议添加前缀（例如 `x-mywidget-`）。