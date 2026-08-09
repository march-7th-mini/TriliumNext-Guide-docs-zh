# 加载数据
数据加载可以在 `doRefresh()` 中完成，因为它能获取到笔记的引用：

```
const blob = await note.getBlob();        
const content = blob.getJsonContent();
```

请注意，当用户进行更改时，`doRefresh` 有时可能会被 <a class="reference-link" href="Saving%20data%20via%20spaced%20update.md">通过间隔更新保存数据</a> 调用，这一点需要考虑在内。