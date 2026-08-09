# Day.js
Day.js 是一个日期操作库，Trilium 使用它，同时它也供前端和后端脚本共用。关于该库本身的更多信息，请查阅[官方文档](https://day.js.org/en/)。

## 如何使用

`dayjs` 方法直接提供在 `api` 全局对象中：

```javascript
const date = api.dayjs();
api.log(date.format("YYYY-MM-DD"));
```

## 插件

Day.js 采用模块化、基于插件的架构。通常这些插件必须导入，但由于使用了打包器，这一过程在 Trilium 脚本内部无法工作。

自 v0.100.0 起，前端和后端脚本均可使用同一组插件。

以下 Day.js 插件已直接集成到 Trilium 中：

*   [AdvancedFormat](https://day.js.org/docs/en/plugin/advanced-format)
*   [Duration](https://day.js.org/docs/en/plugin/duration)，自 v0.100.0 起。
*   [IsBetween](https://day.js.org/docs/en/plugin/is-between)
*   [IsoWeek](https://day.js.org/docs/en/plugin/iso-week)
*   [IsSameOrAfter](https://day.js.org/docs/en/plugin/is-same-or-after)
*   [IsSameOrBefore](https://day.js.org/docs/en/plugin/is-same-or-before)
*   [QuarterOfYear](https://day.js.org/docs/en/plugin/quarter-of-year)
*   [UTC](https://day.js.org/docs/en/plugin/utc)

> [!NOTE]
> 如果出于脚本编写目的需要其他 Day.js 插件，欢迎为其提交功能请求。根据插件的大小以及在 Trilium 代码库中的潜在使用情况，它有可能被集成。