# 体重追踪器
![](Weight%20Tracker_image.png)

`体重追踪器` 是一个 [脚本 API](../../Scripting/Script%20API.md) 演示，存在于 [演示笔记](../Database.md) 中。

通过在 [模板](../Templates.md) 中添加 `weight` 作为 [提升属性](../Attributes/Promoted%20Attributes.md)（[日记笔记](Day%20Notes.md) 由此模板创建），您可以汇总数据并绘制体重随时间变化的图表。

## 实现

上图中的 `体重追踪器` 笔记属于 `渲染笔记` 类型。该类型的笔记本身没有任何实用内容，而是一个占位符，[脚本](../../Scripting.md) 可以在其中渲染其输出。

`渲染笔记` 的脚本通过名为 `~renderNote` 的 [关系](../Attributes.md) 定义。在此示例中，它是 `体重追踪器` 的子笔记 `实现`。该实现由两个 [代码笔记](../../Note%20Types/Code.md) 组成，分别包含一些 HTML 和 JavaScript，用于加载所有带有 `weight` 属性的笔记并将其值显示在图表中。

为了实际渲染图表，我们使用了名为 [chart.js](https://www.chartjs.org/) 的第三方库，它作为附件导入，因为 Trilium 并未内置该库。

### 代码

以下是放置在类型为 `JS 前端` 的 [代码笔记](../../Note%20Types/Code.md) 中的脚本内容：

```
async function getChartData() {
    const days = await api.runOnBackend(async () => {
        const notes = api.getNotesWithLabel('weight');
        const days = [];

        for (const note of notes) {
            const date = note.getLabelValue('dateNote');
            const weight = parseFloat(note.getLabelValue('weight'));

            if (date && weight) {
                days.push({ date, weight });
            }
        }

        days.sort((a, b) => a.date > b.date ? 1 : -1);

        return days;
    });

    const datasets = [
        {
            label: "Weight (kg)",
            backgroundColor: 'red',
            borderColor: 'red',
            data: days.map(day => day.weight),
            fill: false,
            spanGaps: true,
            datalabels: {
                display: false
            }
        }
    ];

    return {
        datasets: datasets,
        labels: days.map(day => day.date)
    };
}

const ctx = $("#canvas")[0].getContext("2d");

new chartjs.Chart(ctx, {
    type: 'line',
    data: await getChartData()
});
```

## 如何从顶部栏移除体重追踪器按钮

在 `体重追踪器` 的链接图中，有一个名为 `按钮` 的笔记。打开它并删除或注释掉其内容。重启 Trilium 后，`体重追踪器` 按钮将消失。