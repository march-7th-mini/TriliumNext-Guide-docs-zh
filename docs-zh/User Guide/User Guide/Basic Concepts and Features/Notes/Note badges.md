# 笔记徽章
笔记徽章显示在固定笔记标题附近，用于指示关于笔记的重要信息，例如笔记是否只读。部分徽章还支持交互操作。

<figure class="image"><img style="aspect-ratio:910/49;" src="Note badges_image.png" width="910" height="49"></figure>

可用的徽章如下：

*   <span class="tn-icon bx bx-lock-alt"></span> **只读徽章**，当笔记因自动只读或手动只读而不可编辑时会显示。点击该徽章将临时编辑笔记。在内置用户指南的页面中（这些页面不可编辑），点击徽章不会有任何操作。
*   <span class="tn-icon bx bx-share-alt"></span> **共享徽章**，用于指示当前笔记已共享。该徽章还会指示共享是在本地网络上（适用于未设置<a class="reference-link" href="../../Installation%20%26%20Setup/Synchronization.md">同步</a>的桌面应用）还是可公开访问（适用于服务器）。
*   <span class="tn-icon bx bx-globe"></span> **网页剪藏徽章**，用于指示笔记是否通过<a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">网页剪藏器</a>剪藏。该徽章充当链接，可点击导航到该页面，或右键单击以获取更多选项。当剪藏器同时保存了页面的描述、作者，或发布与最后更新日期时，点击徽章会改为显示这些详细信息，并在顶部提供指向该页面的链接。
*   <span class="tn-icon bx bx-play"></span> **执行徽章**，用于带有执行按钮或描述的[脚本](../../Scripting.md)或[保存的 SQL 查询](../../Advanced%20Usage/Database/Manually%20altering%20the%20database/SQL%20Console.md)。
*   <span class="tn-icon bx bx-copy-alt"></span> **模板徽章**，用于<a class="reference-link" href="../../Advanced%20Usage/Templates.md">模板</a>（包括工作区模板，此类模板的徽章显示为 _工作区模板_）。从模板创建的笔记会继承其属性，因此该徽章提醒您：更改这些属性会影响所有此类笔记。点击该徽章可在“在所有位置提供”与“仅在提升到其工作区时提供”之间切换模板，后者仅适用于工作区内的模板（参见<a class="reference-link" href="../Navigation/Workspaces.md">工作区</a>）。它还会打开 _模板属性..._，可在其中设置新笔记的默认标题和位置。
*   对于<a class="reference-link" href="../Active%20content.md">活动内容</a>（例如脚本、样式），将显示一个专用徽章，指示笔记类型，并提供轻松启用或禁用它的选项。