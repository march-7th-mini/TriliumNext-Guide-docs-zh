# 本地构建交付物
## 构建桌面端

进入 `apps/desktop`，然后：

*   要生成软件包，运行 `pnpm electron-forge:make`。
*   要仅构建 Flatpak，运行 `pnpm electron-forge:make-flatpak`。
*   要仅构建而不打包，运行 `pnpm electron-forge:package`。

在 macOS 上，打包时会使用 `actool` 编译 Icon Composer 应用图标（`app-icon/icon.icon`、`icon-dev.icon`），因此需要 macOS 26 和 Xcode 26 或更高版本。在较旧版本上，`@electron/packager` 会因 `actool` 错误而失败，而不会回退到 `.icns` 图标。

## 构建服务端

进入 `apps/server` 并运行 `pnpm package` 以执行构建脚本。构建产物将出现在 `apps/server/dist` 中，而打包后的构建则位于 `apps/server/out`。

## 在 NixOS 上

在 NixOS 下需要以下 `nix-shell`：

```
nix-shell -p jq
```

对于 Linux 构建：

```
nix-shell -p jq fakeroot dpkg
```

要测试 Linux 构建，请使用 `steam-run`：

```javascript
$ NIXPKGS_ALLOW_UNFREE=1 nix-shell -p steam-run
[nix-shell] cd dist/trilium-linux-x64
[nix-shell] steam-run ./trilium
```