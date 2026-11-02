# 添加新语言区域

一旦某种语言的 Weblate 翻译覆盖率达到约 50%，就可以将其添加到应用中了。

操作步骤如下：

1.  在 `packages/commons` 中找到 `i18n.ts`，在 `UNSORTED_LOCALES` 中为该语言添加一个新条目。
2.  在 `packages/commons` 中找到 `dayjs.ts`，在 `DAYJS_LOADER` 中为新语言添加映射。对整个列表进行排序。
3.  在 `apps/client` 中找到 `collections/calendar/index.tsx`，修改 `LOCALE_MAPPINGS` 以添加对新语言的支持。
4.  在 `apps/client` 中找到 `widgets/type_widgets/canvas/i18n.ts`，修改 `LANGUAGE_MAPPINGS`。单元测试会确保该语言确实可以加载。
5.  在 `packages/ckeditor5` 中找到 `i18n.ts`，修改 `LOCALE_MAPPINGS`。导入验证应该已经检查了新值是否受 CKEditor 支持，并且也有测试来确保这一点。`i18n.spec.ts` 中的测试是手动逐一固定每个语言区域的，而不是迭代它们，因此也要在那里添加新语言。
6.  在 `apps/client` 中找到 `widgets/type_widgets/spreadsheet/locales.ts`，修改 `UNIVER_LOCALES`，要么提供一个源（如果 Univer 为该语言提供了打包文件），要么显式设置为 `null` 以回退到英语。`SPREADSHEET_PRESET_PACKAGES` 中的每个预设都必须有该语言区域的打包文件，`locales.spec.ts` 会对此进行检查。
7.  PDF.js 的语言区域映射可能需要调整。如需调整，在 `packages/pdfjs-viewer/scripts/build.ts` 中有 `LOCALE_MAPPINGS`。当语言区域的 `electronLocale` 已经指向 `packages/pdfjs-viewer/viewer/locale` 下的某个目录时，则无需添加条目。

步骤 1 到 6 都以 `DISPLAYABLE_LOCALE_IDS` 为键，因此在完成步骤 1 后，`pnpm typecheck` 会报告每一个仍然缺失的条目。

## Electron 语言区域

新条目的 `electronLocale` 指定了桌面应用为该语言保留的 Chromium 语言区域。打包时，`apps/desktop/electron-forge/trim-locales.ts` 中的 `trimElectronLocales` 会删除所有未被任何 `electronLocale` 指定的 Chromium 语言区域文件，并且当某个 `electronLocale` 指定的文件是 Electron 未提供的文件时，构建会失败。选项页面也仅在语言区域具有 `electronLocale` 时才将其列为格式化语言区域。

桌面应用所固定的 Electron 版本的语言区域文件记录在 `apps/desktop/electron-forge/electron-locales.json` 中：

*   如果该语言列在其中（例如 `da.pak` 或 `pt-BR.pak`），将 `electronLocale` 设置为该名称，用下划线代替连字符（`da`、`pt_BR`）。`en-US.pak` 对应 `"en"`。
*   如果未列出，则 Chromium 没有该语言的翻译。将 `electronLocale` 设置为 Chromium 确实提供的某个语言区域，就像爱尔兰语使用 `"en"` 那样，以便该语言仍可作为格式化语言区域提供。

`electronLocale` 只决定打包时保留哪些语言区域文件以及提供哪些语言区域用于格式化。它不决定 Chromium 的语言：`apps/desktop/src/main.ts` 中的 `getElectronLocale()` 将显示语言（或格式化语言区域）的 id 传递给 Chromium 的 `--lang` 开关。

`pnpm --filter desktop test trim-locales` 会针对这些文件运行裁剪，当名称错误时会以 "Locale … was not found in the packaged app" 失败。当文件中记录的 Electron 版本与 `apps/desktop/package.json` 中固定的版本不同时，同一测试规范也会失败；在 Electron 更新后，使用 `pnpm chore:update-electron-locales` 重新生成并提交结果。

## 网站

网站跟踪自己的 Weblate 组件和自己的列表，因此上面添加到应用中的语言区域在添加到网站之前不会在 [triliumnotes.org](https://triliumnotes.org) 上提供。

1.  在 `apps/website` 中找到 `locales.ts`，向 `LOCALES` 添加一个条目，使用该语言自身的名称，并在适用时设置 `rtl`。id 必须与 `apps/website/src/translations` 下的文件夹匹配，该文件夹由 Weblate 创建。
2.  带有区域的语言区域（如 `pt-BR`）由 `i18n.ts` 中的 `mapLocale()` 通过匹配 `LOCALES` 来解析，因此无需进一步映射。中文是例外：它按文字体系选择，而浏览器仅通过区域来报告，`mapLocale()` 对其做了特殊处理。

## 覆盖率门禁

一旦 Weblate 报告某个语言超过 50% 但缺失于任一列表，`scripts/translation/check-translation-coverage.mts` 就会使 CI 失败。它仅在 Weblate 打开的拉取请求上运行，因此引入翻译的拉取请求正是它触发的地方。

该门禁只能捕获已翻译但未提供的语言。它不会注意到已提供但后来落后的语言，也不检查语言区域的渲染效果——只检查 id 是否被列出。