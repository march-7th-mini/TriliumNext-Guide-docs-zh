# 标签

OneNote 的 _标签_ 功能在 Trilium 中通过 <a class="reference-link" href="../../../../Note%20Types/Text/Insert%20buttons/Icons.md">图标</a> 导入，使用默认图标包或 emoji（如果没有合适的替代品）。

> [!IMPORTANT]
> OneNote 的 Graph API 不支持自定义标签，因此 Trilium 无法导入它们。

### 装饰性标签

这些标签保持为段落格式，字形前置到文本中。一个段落可以同时携带多个标签，此时它们的字形会堆叠。

| OneNote 标签 | `data-tag` | 导入为 | 可搜索为 |
| --- | --- | --- | --- |
| Important | `important` | <span class="tn-icon bx bx-star"></span> | `star` |
| Critical | `critical` | <span class="tn-icon bx bx-error-circle"></span> | `error-circle` |
| Question | `question` | <span class="tn-icon bx bx-help-circle"></span> | `help-circle` |
| Highlight | `highlight` | <span class="tn-icon bx bx-highlight"></span> | `highlight` |
| Definition | `remember-for-later` | <span class="tn-icon bx bx-pin"></span> | `pin` |
| Remember for later | `remember-for-later` | <span class="tn-icon bx bx-pin"></span> | `pin` |
| Remember for blog | `remember-for-blog` | <span class="tn-icon bx bx-edit"></span> | `edit` |
| Idea | `idea` | <span class="tn-icon bx bx-bulb"></span> | `bulb` |
| Password | `password` | <span class="tn-icon bx bx-key"></span> | `key` |
| Contact | `contact` | <span class="tn-icon bx bx-user"></span> | `user` |
| Address | `address` | <span class="tn-icon bx bx-home"></span> | `home` |
| Phone number | `phone-number` | <span class="tn-icon bx bx-phone"></span> | `phone` |
| Web site to visit | `web-site-to-visit` | <span class="tn-icon bx bx-globe"></span> | `globe` |
| Source for article | `source-for-article` | <span class="tn-icon bx bx-news"></span> | `news` |
| Send in email | `send-in-email` | <span class="tn-icon bx bx-envelope"></span> | `envelope` |
| Movie to see | `movie-to-see` | <span class="tn-icon bx bx-movie"></span> | `movie` |
| Book to read | `book-to-read` | <span class="tn-icon bx bx-book"></span> | `book` |
| Music to listen to | `music-to-listen-to` | <span class="tn-icon bx bx-music"></span> | `music` |
| Project A | `project-a` | 🅰️ | 🅰️ |
| Project B | `project-b` | 🅱️ | 🅱️ |

### 复选框标签

这些标签变为 <a class="reference-link" href="../../../../Note%20Types/Text/To-do%20Lists.md">待办列表</a>，字形位于条目内部，并保留勾选状态：

| OneNote 标签 | `data-tag` | 导入为 | 可搜索为 |
| --- | --- | --- | --- |
| To Do | `to-do` | _（无）_ | — |
| To Do priority 1 | `to-do-priority-1` | 1️⃣ | 1️⃣ |
| To Do priority 2 | `to-do-priority-2` | 2️⃣ | 2️⃣ |
| Discuss with Person A | `discuss-with-person-a` | <span class="tn-icon bx bx-message-rounded"></span> | `message-rounded` |
| Discuss with Person B | `discuss-with-person-b` | <span class="tn-icon bx bx-message-rounded"></span> | `message-rounded` |
| Discuss with manager | `discuss-with-manager` | <span class="tn-icon bx bx-conversation"></span> | `conversation` |
| Schedule meeting | `schedule-meeting` | <span class="tn-icon bx bx-calendar"></span> | `calendar` |
| Call back | `call-back` | <span class="tn-icon bx bx-phone-call"></span> | `phone-call` |
| Client request | `client-request` | <span class="tn-icon bx bx-clipboard"></span> | `clipboard` |