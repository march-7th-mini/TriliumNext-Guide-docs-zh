# 创建新选项
1.  前往 `options_interface.ts`，将选项添加到 `OptionDefinitions`，并指定其预期的数据类型（布尔值、字符串、数字）。请注意，最终该选项仍将以字符串形式存储，但这有助于在整个应用程序中确保类型安全。
2.  要添加一个带有默认值的新选项，请前往服务器中的 `options_init.ts`，并在 `defaultOptions` 中添加一个新条目。
3.  **使客户端可以调整该选项**  
    默认情况下，选项对客户端不可调整或不可见。为此，请修改 `routes/api/options.ts`，将新添加的选项添加到 `ALLOWED_OPTIONS` 中。