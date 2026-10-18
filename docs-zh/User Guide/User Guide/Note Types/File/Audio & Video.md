# 音频与视频
<figure class="image image-style-align-right image_resized" style="width:61.8%;"><img style="aspect-ratio:953/587;" src="Audio &amp; Video_image.png" width="953" height="587"></figure>

从 v0.103.0 开始，Trilium 为视频和音频文件提供了自定义媒体播放器，其功能比内置播放器更丰富。

v0.103.0 之前的版本也支持媒体文件，但使用的是内置播放器。

文件采用直接流式传输，因此从服务器访问笔记时，无需下载整个文件即可开始播放。

## 关于大型媒体文件的说明

尽管 Trilium 支持媒体文件，但通常不建议用于非常大的文件。上传大型媒体会导致<a class="reference-link" href="../../Advanced%20Usage/Database.md">数据库</a>膨胀，其任何<a class="reference-link" href="../../Installation%20%26%20Setup/Backup.md">备份</a>也会随之膨胀。此外，首次上传文件时可能会出现卡顿。除此之外，大型数据库不应显著影响 Trilium 的整体性能。

## 支持的格式

Trilium 使用浏览器（在桌面端运行时则为 Electron/Chromium）内置的媒体解码机制。从 v0.103.0 开始，当媒体格式不受支持时，将改为显示一条提示信息。

## 交互操作

要播放/暂停，只需点击媒体上的任意位置。对于视频文件，播放后底部控件会自动隐藏，只需移动鼠标即可再次显示。

底部栏具有以下功能：

*   用于在媒体中定位的进度条。最大 60 MB 的音频文件将显示波形进度条，以便直观地概览音轨结构：静音、停顿和较响亮的片段。
*   进度条左侧显示当前时间。
*   进度条右侧显示剩余时间。
*   左侧有以下按钮：
    *   调整播放速度（例如 0.5x、1x）。
    *   播放模式（适用于父笔记中的所有媒体）：
        *   播放一次 — 播放媒体直到结束，然后停止。
        *   循环 — 媒体结束后自动重新播放。
        *   播放下一个 — 当前项目结束后，继续播放同一父笔记中的下一个项目，直到最后一个项目播放完毕。
    *   将视频旋转 90 度（仅限视频）。
*   中间：
    *   上一个媒体 — 跳转到上一个媒体：对于媒体笔记，为树中当前笔记上方最近的媒体笔记（在同一父笔记内）；对于媒体附件，则为上一个媒体附件。
    *   后退 10 秒
    *   播放/暂停
    *   前进 10 秒
    *   下一个媒体 — 跳转到下一个媒体：对于媒体笔记，为树中当前笔记下方最近的媒体笔记（在同一父笔记内）；对于媒体附件，则为下一个媒体附件。
*   右侧：
    *   静音按钮
    *   音量调节
    *   全屏（仅限视频）
    *   缩放填充，将裁剪视频以填满整个窗口（仅限视频）。
    *   画中画，如果浏览器支持（仅限视频）。

## 在笔记中包含媒体

<figure class="image"><img style="aspect-ratio:1395/145;" src="1_Audio &amp; Video_image.png" width="1395" height="145"><figcaption>一个音频笔记包含（配置为“Small”尺寸）。</figcaption></figure>

<a class="reference-link" href="../Text.md">文本</a>和<a class="reference-link" href="../Markdown.md">Markdown</a>笔记可以直接在笔记内容中嵌入交互式媒体播放器。为此，请包含音频或视频文件：

*   **文本笔记：** 在格式工具栏中，点击 _插入_ → _包含_。
*   **Markdown 笔记：** 输入 `/include` 并按 <kbd>Enter</kbd>。

然后选择要包含的音频/视频文件笔记。

## 键盘快捷键

媒体播放器支持以下键盘快捷键：

<table>
    <tbody>
        <tr>
            <td><kbd>Space</kbd></td>
            <td>播放/暂停</td>
        </tr>
        <tr>
            <td><kbd>Left arrow key</kbd></td>
            <td>后退 10 秒</td>
        </tr>
        <tr>
            <td><kbd>Right arrow key</kbd></td>
            <td>前进 10 秒</td>
        </tr>
        <tr>
            <td><kbd>Ctrl</kbd> + <kbd>Left arrow key</kbd></td>
            <td>后退 1 分钟</td>
        </tr>
        <tr>
            <td><kbd>Ctrl</kbd> + <kbd>Right arrow key</kbd></td>
            <td>前进 1 分钟</td>
        </tr>
        <tr>
            <td><kbd>Page Up</kbd></td>
            <td>导航到上一个媒体</td>
        </tr>
        <tr>
            <td><kbd>Page Down</kbd></td>
            <td>导航到下一个媒体</td>
        </tr>
        <tr>
            <td><kbd>F</kbd></td>
            <td>切换全屏</td>
        </tr>
        <tr>
            <td><kbd>M</kbd></td>
            <td>静音/取消静音</td>
        </tr>
        <tr>
            <td><kbd>Home</kbd></td>
            <td>转到媒体开头</td>
        </tr>
        <tr>
            <td><kbd>End</kbd></td>
            <td>转到媒体末尾</td>
        </tr>
        <tr>
            <td><kbd>Up</kbd></td>
            <td>音量增加 5%</td>
        </tr>
        <tr>
            <td><kbd>Down</kbd></td>
            <td>音量减少 5%</td>
        </tr>
        <tr>
            <td><kbd>Alt+F1</kbd>（可自定义）</td>
            <td>在屏幕上显示此键盘快捷键列表。</td>
        </tr>
    </tbody>
</table>