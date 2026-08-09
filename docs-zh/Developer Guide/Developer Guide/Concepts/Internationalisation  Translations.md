# 国际化/翻译

在 Trilium Notes 的初始开发阶段，并未考虑国际化问题，因为其定位为纯英文产品。

随着应用和用户群的不断增长，通过提供用户母语的翻译来触达尽可能多的人群就显得很有必要。

所使用的库是 [i18next](https://www.i18next.com/)。

## 翻译文件在哪里？

翻译文件格式为 JSON 文件，位于 `src/public/translations` 目录下。对于每个支持的语言区域，都有一个子目录，其中包含一个 `translation.json` 文件（例如 `src/public/translations/en/translation.json`）。

### 消息键

一个重要的方面是我们采用了基于键的方法。这意味着每条消息都通过一个 ID 来标识，而不是使用自然语言消息（例如 gettext 中的默认方法）。

基于键的方法允许层级结构。例如，一个 `about.title` 的键会在 `translation.json` 中如下添加：

```json
{
	"about": {
		"title": "关于 Trilium Notes"
	}
} 
```

在创建新消息时，请遵循 <a class="reference-link" href="Internationalisation%20%20Translations/Guidelines.md">指南</a>。

### 添加新的语言区域

参见 <a class="reference-link" href="Internationalisation%20%20Translations/Adding%20a%20new%20locale.md">添加新的语言区域</a>。

### 更改语言

由于国际化进程尚处于早期阶段，目前还没有面向用户的语言切换方式。

要手动更改语言，请编辑 `src/public/app/services/i18n.js` 并查找包含 `lng: "en"` 的行。将 `en` 替换为所需的语言代码（从 `src/public/translations` 中可用的代码中选择）。

## 客户端翻译

### 组件级翻译

大多数客户端翻译存在于各种小组件和布局中。

每个文件都需要手动添加翻译支持。

第一步是使用相对导入添加翻译导入。例如，如果我们位于 `src/public/app/widgets/dialogs` 目录中，导入将如下所示：

```javascript
import { t } from "../../services/i18n.js";
```

之后，只需将硬编码的消息替换为：

```javascript
${t("msgid")}
```

其中 `msgid` 是被翻译消息的键。

### 变量

在翻译中，使用 `{{` 和 `}}` 将变量括起来：

```
{
    "key": "{{what}} 是 {{how}}"
}
```

然后在读取翻译时传递参数：

```
t('key', { what: 'i18next', how: '很棒' })
```

### 模板级翻译

模板是 `src/views` 中的 `.ejs` 文件，用于准备桌面端、移动端应用以及设置（引导）和共享笔记视图的根布局。

由于使用了不同的方法，目前还无法翻译这些文件。

## 服务端翻译

目前服务端消息不可翻译。它们将作为单独的步骤添加。

## 区域/语言选择

语言作为选项存储，并在所有设备间同步，用户可以通过 选项 → 外观 → 区域 进行调整。

目前展示给用户的选项在 `src/routes/api/options.ts` 中是硬编码的，其中有一个 `getSupportedLocales()` 函数。`id` 字段必须与 `src/public/translations` 中对应的目录匹配，`name` 必须是该语言的本地化名称（即名称必须使用该语言本身，而非英语）。