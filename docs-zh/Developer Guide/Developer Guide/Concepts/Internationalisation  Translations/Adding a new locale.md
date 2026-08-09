# 添加新语言环境
一旦某个语言在 Weblate 中的翻译覆盖率达到了约 50%，就可以将其添加到应用程序中。

具体操作如下：

1.  在 `packages/commons` 中找到 `i18n.ts`，在 `UNSORTED_LOCALES` 中为该语言添加一个新条目。
2.  在 `packages/commons` 中找到 `dayjs.ts`，在 `DAYJS_LOADER` 中为新语言添加映射。对整个列表进行排序。
3.  在 `apps/client` 中，找到 `collections/calendar/index.tsx`，修改 `LOCALE_MAPPINGS` 以添加对新语言的支持。
4.  在 `apps/client` 中，找到 `widgets/type_widgets/canvas/i18n.ts`，修改 `LANGUAGE_MAPPINGS`。单元测试会确保该语言确实可以加载。
5.  在 `packages/ckeditor5` 中，找到 `i18n.ts`，修改 `LOCALE_MAPPINGS`。导入验证应已检查新值是否受 CKEditor 支持，并且也有一个测试来确保这一点。`i18n.spec.ts` 中的测试是手动固定每个语言环境，而不是遍历它们，因此请将新语言环境也添加到该测试中。
6.  在 `apps/client` 中，找到 `widgets/type_widgets/spreadsheet/locales.ts`，修改 `UNIVER_LOCALES`，要么使用源（如果 Univer 为该语言提供了包），要么使用显式的 `null` 以回退到英语。`SPREADSHEET_PRESET_PACKAGES` 中的每个预设都必须有该语言环境的包，`locales.spec.ts` 会对此进行检查。
7.  PDF.js 的语言环境映射可能需要调整。为此，在 `packages/pdfjs-viewer/scripts/build.ts` 中有 `LOCALE_MAPPINGS`。当语言环境的 `electronLocale` 已经命名了 `packages/pdfjs-viewer/viewer/locale` 下的一个目录时，则无需添加条目。

步骤 1 到 6 由 `DISPLAYABLE_LOCALE_IDS` 作为键控，因此在步骤 1 之后，`pnpm typecheck` 会报告每个仍然缺失的条目。