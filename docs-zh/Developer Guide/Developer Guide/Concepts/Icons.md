# 图标

图标存储在 `images` 和 `images/app-icons` 目录中。

## 网站图标

网站图标通过 `serve-favicon` 动态提供，使用的是 `images/app-icons/win/icon.ico` 中的图标。

## 图标的声明式生成

目前所有图标都是基于 `images` 目录中的 SVG 文件，使用 `bin/create-icons.sh` 脚本构建而成。

## 主要图片

这些图片存储在 `images` 目录中：

| 名称 | 分辨率 | 描述 |
| --- | --- | --- |
| `icon-black.svg` | 53x40 | 用于全局菜单按钮未悬停时。 |
| `icon-color.svg` | 53x40 | 用于全局菜单悬停时。 |
| `icon-grey.svg` | 53x40 | 用于深色主题，替代 `icon-black.svg`。 |

## 应用图标

<table>
    <thead>
        <tr>
            <th>名称</th>
            <th>分辨率</th>
            <th>描述</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>ios/apple-touch-icon.png</code></td>
            <td>180x180</td>
            <td>用作 <code>apple-touch-icon</code>，但出于某种原因，仅在 <code>login.ejs</code> 和 <code>set_password.ejs</code> 中使用。</td>
        </tr>
        <tr>
            <td><code>mac/icon.icns</code></td>
            <td>512x512</td>
            <td>作为 <code>--icon</code> 参数提供给 <code>electron-packager</code>，用于 <code>mac-arm64</code> 和 <code>mac-x64</code> 的 <a href="../Building/Build%20deliveries%20locally.md">构建</a>。</td>
        </tr>
        <tr>
            <td><code>png/128x128.png</code></td>
            <td>128x128</td>
            <td>用于 <code>linux-x64</code> <a href="../Building/Build%20deliveries%20locally.md">构建</a>，以提供 <code>icon.png</code>。</td>
        </tr>
        <tr>
            <td><code>png/256x256-dev.png</code></td>
            <td>256x256</td>
            <td>用于 Electron 窗口图标（如果在开发模式下）。</td>
        </tr>
        <tr>
            <td><code>png/256x256.png</code></td>
            <td>用于 Electron 窗口图标（如果不在开发模式下）。</td>
        </tr>
        <tr>
            <td><code>win/icon.ico</code></td>
            <td><ul><li>ICO 16x16</li><li>ICO 32x32</li><li>ICO 48x48</li><li>ICO 64x64</li><li>ICO 128x128</li><li>PNG 256x256</li></ul></td>
            <td><ul><li>用于 <code>win-x64</code> <a href="../Building/Build%20deliveries%20locally.md">构建</a>。</li><li>被 Squirrel Windows 安装程序用于：安装程序图标、应用程序图标、控制面板图标</li><li>用作网站图标。</li></ul></td>
        </tr>
        <tr>
            <td><code>win/setup-banner.gif</code></td>
            <td>640x480</td>
            <td>在安装过程中由 Squirrel Windows 安装程序使用。仅有一帧。</td>
        </tr>
    </tbody>
</table>

## 品牌标识的其他使用位置

*   在客户端中，更具体地说是在 `src/public/app/widgets/buttons/global_menu.js` 中，图标的 SVG 内容被直接嵌入以允许通过 CSS 进行样式设置。
*   在 <a class="reference-link" href="Demo%20document.md">演示文档</a> 中，作为附件。
*   在 <a class="reference-link" href="#root/OeKBfN6JbMIq/MF99QFRe1gVy/xkj1bqW7zJwQ/t6mT72MfEzb2">CKEditor</a> 构建中，查找 `packages/ckeditor5-build-balloon-block/src/icons/trilium.svg`。确保 SVG 中没有任何 `fill` 覆盖，否则会使用错误的颜色。