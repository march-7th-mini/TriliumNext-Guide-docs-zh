# 服务器翻译

*   服务器端的翻译与客户端一样，由同一个库 i18next 管理。
*   翻译文件位于 `/translations` 目录，遵循与客户端相同的约定（`translations/{{lng}}/{{ns}}.json`），其中命名空间为 `server.json`。因此，对于西班牙语翻译，我们有 `translations/es/server.json`。
*   翻译的加载由 [i18next-fs-backend](https://github.com/i18next/i18next-fs-backend) 管理，它直接从文件系统（不像客户端那样通过 HTTP 请求）加载翻译，路径如前所述（相对于 `package.json`）。

## 如何翻译字符串

与使用专用客户端服务的客户端不同，服务器上直接使用 i18next 库，如下所示：

```javascript
import { t } from "i18next";

const translatedString = t("message.id");
```

## 应该翻译什么

*   避免翻译服务器端日志，因为这些日志主要用于调试，翻译它们没有益处。
*   翻译任何来自服务器、面向用户的消息，例如 Electron 应用程序中显示的错误消息，或键盘快捷键、笔记标题等信息。