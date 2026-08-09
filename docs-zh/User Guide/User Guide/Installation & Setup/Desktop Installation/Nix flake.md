# Nix flake
自 TriliumNext 0.94.1 起，桌面版和服务器版应用均可使用 [Nix](https://nixos.org/) 构建。

## 系统要求

在 Mac 或 Linux 上安装 Nix（[下载页面](https://nixos.org/download/)）。需要约 3-4 GB 的额外存储空间，用于存放构建产物。

## 直接运行

使用 [nix run](https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-run.html)，桌面应用可通过以下命令启动：`nix run github:TriliumNext/Trilium/v0.95.0`

运行服务器需要显式指定所需的包：`nix run github:TriliumNext/Trilium/v0.95.0#server`

除了版本号（如上文的 `v0.95.0`），您也可以指定提交哈希（或分支名称）。这样可以方便地测试开发版本。

## 在 NixOS 上安装

添加到您的 `flake.nix`：

```
{
  inputs = {
    nixpkgs.url = # ...;
    trilium-notes = {
      url = "github:TriliumNext/Trilium/v0.95.0";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      self,
      # ...
      trilium-notes,
      ...
    }:
    {
      nixosConfigurations = {
        "nixos" = nixpkgs.lib.nixosSystem {
          system = "x86_64-linux";
          modules = [
            ./configuration.nix
          ];
          specialArgs = {
            inherit
              trilium-notes
              ;
          };
        };
      };
    };
}

```

添加到您的 `configuration.nix`：

```
{
  # ...
  trilium-notes,
  ...
}:

{
  # ...

  services.trilium-server.package = trilium-notes.packages.x86_64-linux.server;

  environment.systemPackages = [
    trilium-notes.packages.x86_64-linux.desktop
  ];
}
```

该 flake 旨在与最新的 NixOS 稳定版和不稳定版兼容。