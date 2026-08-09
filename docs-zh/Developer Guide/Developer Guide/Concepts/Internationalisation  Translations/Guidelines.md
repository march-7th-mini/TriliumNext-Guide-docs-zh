# 指南
*   在适当的情况下使用层级结构，尝试按以下方式对消息进行分组：
    *   模态框（例如 `about.foo`、`jump_to_note.foo`）
*   不要重复使用非常广泛的消息。
    *   一个例子是 `aria-label="Close"`，它应该放在一个单一的消息中，如 `modal.close`，而不是在每个模态框中重复。
*   另一方面，不要过度泛化消息。一个 `close` 消息在遇到“关闭”这个词时就被使用并不是一个好方法，因为缺乏上下文可能会导致问题。
*   在适当的情况下使用[变量插值](https://www.i18next.com/translation-function/interpolation)。
    *   如果你看到多个消息只是为了应用一个变量（如用户输入的值）而连接在一起，尝试将这些消息合并成一个包含变量的单一消息。
    *   因此，不要使用 `“Number of updates: “ + numUpdates + “.”`，而是使用 `$(t("number_updates", { numUpdates }))`，其中消息翻译将显示为 `Number of updates: {{numUpdates}}.`