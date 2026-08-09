# 字数统计小组件

> [!TIP]
> 此小组件也包含在新安装的 <a class="reference-link" href="../../../Advanced%20Usage/Database/Demo%20Notes.md">演示笔记</a> 中。

创建一个类型为 JavaScript（Trilium 前端）的 <a class="reference-link" href="../../../Note%20Types/Code.md">代码</a> 笔记，并**为其添加** `#widget` **标签**。

```
/*
 * 此代码定义了一个自定义小组件，用于显示当前文本笔记中的字数和字符数。
 * 要为特定笔记激活此功能，请为该笔记添加 'wordCount' 标签，您也可以将其设为可继承，从而为整个子树激活此功能。
 * 
 * 可在“书籍”及其子树中查看其实际效果。
 */
const TPL = `<div style="padding: 10px; border-top: 1px solid var(--main-border-color); contain: none;">
    <strong>字数： </strong>
    <span class="word-count"></span>

    &nbsp;

    <strong>字符数： </strong>
    <span class="character-count"></span>
</div`;

class WordCountWidget extends api.NoteContextAwareWidget {
    get position() { return 100; } // 值越大表示位置越靠底部/右侧
    
    get parentWidget() { return 'center-pane'; }
    
    doRender() {
        this.$widget = $(TPL);
        this.$wordCount = this.$widget.find('.word-count');
        this.$characterCount = this.$widget.find('.character-count');
        return this.$widget;
    }
    
    async refreshWithNote(note) {
        if (note.type !== 'text' || !note.hasLabel('wordCount')) { 
            // 仅在文本笔记且标记有 'wordCount' 标签时显示小组件
            this.toggleInt(false); // 隐藏
            
            return;
        }
        
        this.toggleInt(true); // 显示
        
        const {content} = await note.getNoteComplement();
        
        const text = $(content).text(); // 仅获取纯文本
        
        const counts = this.getCounts(text);

        this.$wordCount.text(counts.words);
        this.$characterCount.text(counts.characters);
    }
    
    getCounts(text) {
        const chunks = text
            .split(/[\s-+:,/\\]+/)
            .filter(chunk => chunk !== '');
        
        let words;
        
        if (chunks.length === 1 && chunks[0] === '') {
            words = 0;
        }
        else {
            words = chunks.length;
        }
        
        const characters = chunks.join('').length;
        
        return {words, characters};
    }
    
    async entitiesReloadedEvent({loadResults}) {
        if (loadResults.isNoteContentReloaded(this.noteId)) {
            this.refresh();
        }
    }
}

module.exports = new WordCountWidget();
```

修改后，需要 [重启 Trilium](../../../Troubleshooting/Refreshing%20the%20application.md) 才能重建布局。

该小组件仅在带有 `#wordCount` 标签的文本笔记上激活。此标签可以是一个 [引用链接](../../../Note%20Types/Text/Links/Internal%20\(reference\)%20links.md)，以便为整个子树启用该小组件。

在笔记底部，您可以看到生成的小组件：

<figure class="image"><img style="aspect-ratio:792/603;" src="Word count widget_image.png" width="792" height="603"></figure>