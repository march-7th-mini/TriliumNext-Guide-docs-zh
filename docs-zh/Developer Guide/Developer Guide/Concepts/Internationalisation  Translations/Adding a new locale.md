# 添加新语言区域

一旦 Weblate 上某个单一语言的翻译覆盖率达到约 50%，就可以将其添加到应用中了。

具体操作如下：

1.  在 `packages/commons` 中找到 `i18n.ts`，在 `UNSORTED_LOCALES` 中为该语言添加一个新条目。
2.  在 `packages/commons` 中找到 `dayjs.ts`，在 `DAYJS_LOADER` 中为新语言添加映射。对整个列表进行排序。
3.  在 `apps/client` 中找到 `collections/calendar/index.tsx`，修改 `LOCALE_MAPPINGS` 以添加对新语言的支持。
4.  在 `apps/client` 中找到 `widgets/type_widgets/canvas/i18n.ts`，修改 `LANGUAGE_MAPPINGS`。有一个单元测试确保该语言确实可以加载。
5.  在 `packages/ckeditor5` 中找到 `i18n.ts`，修改 `LOCALE_MAPPINGS`。导入验证应该已经检查了新值是否受 CKEditor 支持，并且还有一个测试来确保这一点。`i18n.spec.ts` 中的测试是手动固定每个语言区域而非遍历它们，因此也要在那里添加新语言区域。
6.  在 `apps/client` 中找到 `widgets/type_widgets/spreadsheet/locales.ts`，修改 `UNIVER_LOCALES`，可以使用源（如果 Univer 为该语言提供了打包文件），也可以显式设置为 `null` 以回退到英语。`SPREADSHEET_PRESET_PACKAGES` 中的每个预设都必须有该语言区域的打包文件，`locales.spec.ts` 会对此进行检查。
7.  PDF.js 的语言区域映射可能需要调整。如需调整，在 `packages/pdfjs-viewer/scripts/build.ts` 中有 `LOCALE_MAPPINGS`。当语言区域的 `electronLocale` 已经指向 `packages/pdfjs-viewer/viewer/locale` 下的某个目录时，则无需添加条目。

步骤 1 到 6 都以 `DISPLAYABLE_LOCALE_IDS` 为键，因此在完成步骤 1 后，`pnpm typecheck` 会报告每个仍然缺失的项。

## 网站

网站跟踪自己的 Weblate 组件和自己的列表，因此在上面的应用中添加的语言区域，在添加到网站之前不会在 [triliumnotes.org](https://triliumnotes.org) 上提供。

1.  在 `apps/website` 中找到 `locales.ts`，在 `LOCALES` 中添加一个条目，使用该语言自身的名称，并在适用时设置 `rtl`。id 必须与 `apps/website/src/translations` 下的文件夹匹配，该文件夹由 Weblate 创建。
2.  带有区域的语言区域（如 `pt-BR`）由 `i18n.ts` 中的 `mapLocale()` 通过匹配 `LOCALES` 来解析，因此无需进一步映射。中文是例外：它按文字系统选择，而浏览器仅通过区域来报告，`mapLocale()` 对其做了特殊处理。

## 覆盖率门禁

一旦 Weblate 报告某个语言超过 50% 但缺失于任一列表，`scripts/translation/check-translation-coverage.mts` 就会使 CI 失败。它仅在 Weblate 打开的拉取请求上运行，因此引入翻译的那个拉取请求就是它触发的地方。

该门禁只能捕获已翻译但未提供的语言。它不会注意到已提供但此后落后的语言，也不会检查语言区域是否能够渲染——只检查 id 是否已列出。