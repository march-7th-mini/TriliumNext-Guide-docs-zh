# 添加新语言环境

一旦 Weblate 中某种语言的翻译覆盖率达到了约 50%，就可以将其添加到应用程序中。

具体步骤如下：

1.  在 `packages/commons` 中找到 `i18n.ts`，在 `UNSORTED_LOCALES` 中为该语言添加一个新条目。
2.  在 `packages/commons` 中找到 `dayjs.ts`，在 `DAYJS_LOADER` 中为新语言添加映射。对整个列表进行排序。
3.  在 `apps/client` 中，找到 `collections/calendar/index.tsx`，修改 `LOCALE_MAPPINGS` 以添加对新语言的支持。
4.  在 `apps/client` 中，找到 `widgets/type_widgets/canvas/i18n.ts`，修改 `LANGUAGE_MAPPINGS`。单元测试会确保该语言确实可以被加载。
5.  在 `packages/ckeditor5` 中，找到 `i18n.ts`，修改 `LOCALE_MAPPINGS`。导入验证应该会检查新值是否受 CKEditor 支持，并且还有一个测试来确保这一点。`i18n.spec.ts` 中的测试是手动固定每个语言环境的，而不是遍历它们，所以也要在那里添加新的语言环境。
6.  在 `apps/client` 中，找到 `widgets/type_widgets/spreadsheet/locales.ts`，修改 `UNIVER_LOCALES`，可以提供一个来源（如果 Univer 为该语言提供了捆绑包），或者显式设置为 `null` 以回退到英语。`SPREADSHEET_PRESET_PACKAGES` 中的每个预设都必须有该语言环境的捆绑包，`locales.spec.ts` 会对此进行检查。
7.  PDF.js 的语言环境映射可能需要调整。为此，在 `packages/pdfjs-viewer/scripts/build.ts` 中有 `LOCALE_MAPPINGS`。当语言环境的 `electronLocale` 已经命名了 `packages/pdfjs-viewer/viewer/locale` 下的一个目录时，则无需添加条目。

步骤 1 到 6 以 `DISPLAYABLE_LOCALE_IDS` 为键，因此在步骤 1 之后，`pnpm typecheck` 会报告每个仍然缺失的项。

## 网站

网站跟踪其自己的 Weblate 组件和列表，因此上述添加到应用程序中的语言环境在添加到 [triliumnotes.org](https://triliumnotes.org) 之前，不会在该网站上提供。

1.  在 `apps/website` 中，找到 `locales.ts`，在 `LOCALES` 中添加一个条目，使用该语言自身的名称，并在适用的情况下设置 `rtl`。该 id 必须与 `apps/website/src/translations` 下的文件夹匹配，该文件夹由 Weblate 创建。
2.  带有区域的语言环境（例如 `pt-BR`）由 `i18n.ts` 中的 `mapLocale()` 通过匹配 `LOCALES` 来解析，因此无需进一步映射。中文是个例外：它是通过脚本选择的，浏览器只能通过区域来报告，而 `mapLocale()` 对其进行了特殊处理。

## 覆盖率门槛

一旦 Weblate 报告某种语言翻译率超过 50%，但该语言在任一列表中缺失，`scripts/translation/check-translation-coverage.ts` 就会导致 CI 失败。它在 `weblate:*` 分支上运行，因此引入翻译的拉取请求就是它触发的地方。

该门槛只会捕获已翻译但未提供的语言。它不会注意到已提供但后来落后的语言，也不会检查语言环境是否能正常渲染——只检查 id 是否在列表中。