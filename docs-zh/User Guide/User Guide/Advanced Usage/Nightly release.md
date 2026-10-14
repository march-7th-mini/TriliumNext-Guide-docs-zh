# 每日构建版本
每日构建版本是每天构建的版本，包含最新的改进和错误修复，直接来自主开发分支。这些版本通常有助于为正式发布做准备，确保没有需要优先解决的重大错误，也可以用来确认某个特定错误是否已修复或某个功能是否已良好实现。

## 关于稳定性

尽管处于开发分支，但主分支通常相当稳定，因为 PR 在合并前都会经过测试。如果您发现任何问题，欢迎通过工单或 Matrix 进行反馈。

## 手动下载每日构建版本

前往 [github.com/TriliumNext/Trilium/releases/tag/nightly](https://github.com/TriliumNext/Trilium/releases/tag/nightly)，查找以 `TriliumNotes-main` 开头的构建产物。选择适合您平台的版本（例如 `windows-x64.zip`）。

根据您的使用场景，您可以选择测试便携版，甚至使用安装程序。

> [!NOTE]
> 如果您选择可安装版本（例如 Windows 上的 .exe），它将替换您的稳定版安装。

> [!IMPORTANT]
> 默认情况下，每日构建版本使用与生产版本相同的数据库。通常您可以根据需要轻松降级。但是，如果数据库或同步版本发生了变化，则必须从备份恢复才能降级。

## 自动下载并安装最新的每日构建版本

如果您是希望定期更新版本的 Beta 测试者，这将非常有用：

=== "<span class="tn-icon bx bxl-tux"></span> Ubuntu (Bash)"

    ```sh
    #!/usr/bin/env bash

    name=TriliumNotes-linux-x64-nightly.deb
    rm -f $name*
    wget https://github.com/TriliumNext/Trilium/releases/download/nightly/$name
    sudo apt-get install ./$name
    rm $name
    ```

=== "<span class="tn-icon bx bxl-windows"></span> Windows (PowerShell)"

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