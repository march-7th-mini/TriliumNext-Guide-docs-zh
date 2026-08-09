# 夜间版

夜间版是每天构建的版本，包含来自主开发分支的最新改进和错误修复。这些版本通常在准备发布时很有用，可以确保没有需要优先处理的重要错误，或者可以用来确认某个特定错误是否已修复或某个功能是否已正确实现。

## 关于稳定性

尽管位于开发分支上，但主分支通常相当稳定，因为拉取请求在合并之前已经过测试。如果您发现任何问题，请随时通过工单或 Matrix 报告。

## 手动下载夜间版

前往 [github.com/TriliumNext/Trilium/releases/tag/nightly](https://github.com/TriliumNext/Trilium/releases/tag/nightly) 并查找以 `TriliumNotes-main` 开头的构建产物。选择适合您平台的那个（例如 `windows-x64.zip`）。

根据您的使用场景，您可以测试便携版，甚至可以使用安装程序。

> [!NOTE]
> 如果您选择可安装版本（例如 Windows 上的 .exe），它将替换您的稳定安装。

> [!IMPORTANT]
> 默认情况下，夜间版使用与生产版本相同的数据库。通常，如果需要，您可以轻松降级。但是，如果数据库或同步版本有更改，则必须从备份中恢复才能降级。

## 自动下载并安装最新的夜间版

如果您是希望定期更新版本的测试人员，这将非常有用：

## 在 Ubuntu 上（Bash）

```sh
#!/usr/bin/env bash

name=TriliumNotes-linux-x64-nightly.deb
rm -f $name*
wget https://github.com/TriliumNext/Trilium/releases/download/nightly/$name
sudo apt-get install ./$name
rm $name
```

## 在 Windows 上（PowerShell）

```powershell
if ($env:PROCESSOR_ARCHITECTURE -eq "ARM64") {
  $arch = "arm64";
} else {
  $arch = "x64";
}

$exeUrl = "https://github.com/TriliumNext/Trilium/releases/download/nightly/TriliumNotes-main-windows-$($arch).exe";
Write-Host "Downloading $($exeUrl)"

# Generate a unique path in the temp dir
$guid = [guid]::NewGuid().ToString()
$destination = Join-Path -Path $env:TEMP -ChildPath "$guid.exe"

try {
    $ProgressPreference = 'SilentlyContinue'
    Invoke-WebRequest -Uri $exeUrl -OutFile $destination
    $process = Start-Process -FilePath $destination
} catch {
    Write-Error "An error occurred: $_"
} finally {
    # Clean up
    if (Test-Path $destination) {
        Remove-Item -Path $destination -Force
    }
}
```