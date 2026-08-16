# 编辑器内 AI 助手

<figure class="image image-style-align-center image_resized" style="width:76.29%;"><img style="aspect-ratio:1479/865;" src="In-editor AI assistant_image.png" width="1479" height="865"></figure>

AI 助手作用于您正在编写的文本：选中一段文字，即可让它重写、翻译或转换为表格，也可以在光标处请求生成新内容。与 [AI对话](../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar/AI%20chat%20tab.md) 不同，它不会打开对话窗口，结果会就地预览，只有在您接受后才会写入笔记。

## 要求

只有在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / 大语言模型_ 中配置了至少一个提供商，并为其选择了至少一个模型后，助手才可用。在此之前，工具栏条目完全不会显示。

## 访问 AI 助手

要访问 AI 助手：

*   在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中查找 <img class="image_resized" style="aspect-ratio:150/150;width:3.16%;" src="In-editor AI assistant_ai.svg" width="150" height="150"> 按钮。按下按钮本身进入 _Ask AI_ 模式，或按下旁边的箭头键访问快速命令和模型选择。
*   在<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>中查找 _AI 助手_ 或任何以 _AI_ 为前缀的快速命令。
*   按下 <kbd spellcheck="false">Ctrl</kbd>+<kbd spellcheck="false">Shift</kbd>+<kbd spellcheck="false">K</kbd>。
*   在桌面应用中，在文本中右键单击并选择 _AI 助手_ 选项。

## 助手处理的内容

| 情况 | 发送的内容 |
| --- | --- |
| 已选择文本 | 选中的内容。 |
| 未选择文本，且您选择了快速操作 | 光标所在的段落。 |
| 未选择文本，且您输入了自己的提示词 | 无，响应是在光标处生成的新内容。 |

在所有情况下，助手还会发送目标文本前后的内容，以便模型能够了解其写入的上下文：当要求 _继续写作_ 或总结时，只能看到选中词语的模型是在猜测其周围的文档内容。这些周围文本仅作为上下文，绝不会被重写。

> [!IMPORTANT]
> 这意味着单次运行发送的内容会超过您高亮显示的段落。具体哪些数据会离开您的机器，请参阅 <a class="reference-link" href="../../AI/Privacy.md">隐私</a>。

## 快速操作

工具栏按钮旁边的箭头会打开一个包含预设指令的菜单，按功能分组。

*   _重新格式化_ 操作会生成真正的 Trilium 内容，而非纯文本：_图表_ 插入 Mermaid 图表，_标注_ 插入警示框，_折叠块_ 插入可折叠块。
*   _翻译_ 组列出您已启用的[内容语言](Content%20language%20%26%20Right-to-left%20support.md)，如果未设置内容语言，则显示预定义列表。该列表可在编辑器内填充，子菜单的最后一项可直接打开语言配置。

需要处理对象的操作在无对象可处理时会变灰（例如，空段落且无选中内容）。

## 请求特定操作

选择 _Ask AI…_ 会打开一个提示框，您可以在其中用自己的话描述更改，例如：“让这更不正式”、“为 2024 添加一行”、“为这部分写一个引言段落”。按 <kbd spellcheck="false">Enter</kbd> 或发送按钮运行。

一旦收到响应，您可以在同一提示框中继续操作，助手会将其视为对话而非新请求：在 _翻译成德语_ 之后，要求 _让它更短_ 会缩短德语文本，而不是原始文本。

## 审阅结果

响应会流式生成，可随时按 _停止_ 按钮中断；在此之前到达的内容仍然可用。

在您确认之前，不会有任何内容写入笔记。审阅提供以下选项：

*   **结果** 显示将按插入方式呈现的响应。
*   **更改** 显示与原始文本的内联差异，并标记插入和删除。当模型重写了段落而非编辑时，审阅会改为在 _结果_ 上打开：两份共同点很少的文本的差异比答案本身更难阅读。
*   **重试**，重新运行相同的指令。
*   **替换**，替换原始段落。
*   **在下方插入**，保留原始内容并在其后添加响应。

Trilium 还会报告生成响应的模型、消耗的令牌数，以及对于支持报告的提供商，还会报告价格。

如果您请求更正但无需更正，助手会明确提示，而不是显示空白的差异。

## 选择模型

快速操作菜单底部显示助手运行的模型，并允许您从在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / 大语言模型_ 中选择的模型中选择另一个，按提供商分组。

在请求特定操作时，或在助手生成响应后（例如，响应需要更好的模型时），也可以更改模型。

此选择与对话使用的模型无关，并会在笔记和设备间被记住。如果未设置，助手将遵循第一个配置的提供商。