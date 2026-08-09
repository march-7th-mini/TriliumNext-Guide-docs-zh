# 主题

## 服务端

*   应用程序内置了三个主题：
    *   `light`，位于 `src\public\stylesheets\theme-light.css`
    *   `dark`，位于 `src\public\stylesheets\theme-dark.css`
    *   `next`，由 `src\public\stylesheets\theme-next-light.css` 和 `src\public\stylesheets\theme-next-dark.css` 组成。
*   默认主题仅在创建数据库时设置一次，并由 `options_init#initNotSyncedOptions` 管理。
    *   在原始实现中：在 Electron 上，`light` 和 `dark` 的选择基于操作系统偏好。否则，主题始终为 `dark`。
    *   现在，我们始终选择 `next` 作为默认主题。
*   主题通过 `src\routes\index.ts` 中的 `getThemeCssUrl` 方法提供。

## 客户端

*   预定义主题在客户端的 `src\public\app\widgets\type_widgets\options\appearance\theme.js` 中硬编码。
*   用户自定义主题通过调用服务器获取：`options/user-themes`。
*   主题检索通过请求完成。