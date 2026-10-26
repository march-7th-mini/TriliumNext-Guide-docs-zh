# 隐藏笔记
<figure class="image image-style-align-right"><img style="aspect-ratio:263/445;" src="Hidden Notes_image.png" width="263" height="445"></figure>

为了便于扩展，Trilium 中的许多功能利用实际的笔记来存储信息，而不是将它们存储在数据库中的单独位置。这使得诸如<a class="reference-link" href="Attributes.md">属性</a>、<a class="reference-link" href="Attributes/Relations.md">关系</a>，甚至<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>和<a class="reference-link" href="../Note%20Types/Text/Links.md">链接</a>等功能能够对它们进行操作。

顾名思义，这些笔记默认对用户隐藏，以防止笔记树变得杂乱，并防止它们被意外删除。

隐藏笔记与普通笔记一样存储在用户的<a class="reference-link" href="Database.md">数据库</a>中，但它们具有唯一的<a class="reference-link" href="Note%20ID.md">笔记 ID</a>，从而可以与普通笔记区分开来。

## 访问隐藏笔记树

从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>中，选择 _高级_ → _隐藏笔记_。

## 隐藏笔记树的内容

以下是隐藏树中所有笔记的简要概述：

<table class="ck-table-resized">
    <colgroup>
        <col style="width:19.93%;">
        <col style="width:80.07%;">
    </colgroup>
    <thead>
        <tr>
            <th>笔记</th>
            <th>描述</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_globalNoteMap">笔记地图</a></td>
            <td><p>此笔记实际上是在从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>访问<a class="reference-link" href="../Note%20Types/Note%20Map.md">笔记地图</a>功能时打开的。</p><p>可以在其中创建任何子笔记，而不会有任何额外的含义。例如，它可用于存储笔记地图列表，这些列表可以从其他笔记链接到或被<a href="../Basic%20Concepts%20and%20Features/Navigation/Bookmarks.md">书签</a>收藏。</p></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_sqlConsole">SQL 控制台历史</a></td>
            <td><p>当在<a class="reference-link" href="Database/Manually%20altering%20the%20database/SQL%20Console.md">SQL 控制台</a>中执行 SQL 查询或命令时，它们会存储在此处，按月份分组。仅存储查询，不存储结果。</p><p>无需进入隐藏树即可访问此部分，只需转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>并选择 高级 → SQL 控制台历史。</p><p>可以将笔记添加为此树的子笔记，但通常不建议这样做，以免干扰正常的历史记录过程。</p></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_search">搜索历史</a></td>
            <td><p>每当从完整<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>中执行搜索时，查询将存储在此处，按月份分组。仅存储搜索参数，不存储结果本身。</p><p>无需进入隐藏树即可访问此部分，只需转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>并选择 高级 → 搜索历史。</p><p>可以将笔记添加为此树的子笔记，但通常不建议这样做，以免干扰正常的历史记录过程。</p></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_bulkAction">批量操作</a></td>
            <td><p>此部分用于<a class="reference-link" href="Bulk%20Actions.md">批量操作</a>。批量操作的最后配置将作为此笔记的一部分存储，每个操作位于其自己的 <code>action</code> 标签中。</p><p>可以将笔记添加为此树的子笔记，但这样做没有任何好处。</p></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_backendLog">后端日志</a></td>
            <td><p>此笔记对应于后端日志功能（参见<a class="reference-link" href="../Troubleshooting/Error%20logs.md">错误日志</a>）。</p><p>无需进入隐藏树即可访问此项，只需转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>并选择 高级 → 后端日志。</p></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_userHidden">用户隐藏</a></td>
            <td>此部分可供<a href="../Scripting.md">脚本</a>使用，以创建不应直接对用户可见的自己的笔记。脚本可以通过其唯一 ID 识别该笔记：<code>_userHidden</code></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_lbTplRoot">启动栏模板</a></td>
            <td><p>此部分包含用于在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>中创建启动器的模板。无法在此处创建子笔记。</p><p>理论上，此处的一些笔记可以自定义，但这样做没有太多好处。</p></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_share">共享笔记</a></td>
            <td><p>此树列出了所有公开<a href="Sharing.md">共享</a>的笔记。它可用于追踪哪些笔记被共享，无论它们在笔记树中的位置如何。</p><p>无需进入隐藏树即可访问此部分，只需转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>并选择 <em>高级</em> → <em>共享笔记</em>。</p><p>无法在此处创建子笔记。</p></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_lbRoot">启动栏</a></td>
            <td><p>此树包含<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>的可用项和显示项。</p><p>无需进入隐藏树即可访问此部分，方法如下：</p><ul><li>转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>并选择 <em>配置启动栏…</em>。</li><li>右键单击<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>上的空白区域，然后选择 <em>配置启动栏…</em>。</li></ul><p>无法在此处创建子笔记。</p></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_options">选项</a></td>
            <td><p>此部分存储<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>的列表。</p><p>无需进入隐藏树即可访问此部分，方法如下：</p><ul><li>转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>并选择 <em>选项</em>。</li><li>按下<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>中专用的选项图标。</li></ul></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_lbMobileRoot">移动端启动栏</a></td>
            <td><p>这与 <em>启动栏</em> 非常相似，但专用于移动端 UI。</p><p>在 <em>启动栏</em> 之外访问它的方式与启动栏相同，但需要从移动端界面进行操作。</p></td>
        </tr>
        <tr>
            <td><a class="reference-link" href="#root/_hidden/_help">用户指南</a></td>
            <td>这是用户指南在笔记树中出现的位置。其笔记不存储在数据库中：Trilium 在每次启动时从随应用程序附带的文件构建它们，因此它们无法被编辑、移动或克隆，也不会被同步。</td>
        </tr>
    </tbody>
</table>