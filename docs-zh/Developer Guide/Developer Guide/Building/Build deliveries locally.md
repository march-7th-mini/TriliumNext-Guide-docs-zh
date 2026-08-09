# 本地构建交付物

## 构建桌面版

进入 `apps/desktop` 目录，然后：

*   要生成安装包，运行 `pnpm electron-forge:make`。
*   仅构建 Flatpak 包，运行 `pnpm electron-forge:make-flatpak`。
*   仅构建而不打包，运行 `pnpm electron-forge:package`。

## 构建服务器版

进入 `apps/server` 目录并运行 `pnpm package` 来执行构建脚本。构建产物将出现在 `apps/server/dist` 目录中，而打包后的构建版本则位于 `apps/server/out` 目录。

## 在 NixOS 上

在 NixOS 下，需要以下 `nix-shell`：

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