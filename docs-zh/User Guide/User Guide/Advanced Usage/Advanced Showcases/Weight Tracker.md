# 体重追踪器
![](Weight%20Tracker_image.jpg)

`Weight Tracker` 是一个 [Script API](../../Scripting/Script%20API.md) 展示示例，存在于[演示笔记](../Database.md)中。

通过在创建[日记笔记](Day%20Notes.md)的[模板](../Templates.md)中将 `weight` 添加为[提升属性](../Attributes/Promoted%20Attributes.md)，你可以聚合数据并绘制体重随时间的变化。

## 实现

上图中的 `Weight Tracker` 笔记类型为 `Render Note`。该类型的笔记本身没有任何有用的内容。相反，它是一个占位符，[脚本](../../Scripting.md)可以在其中渲染其输出。

`Render Notes` 的脚本定义在一个名为 `~renderNote` 的[关系](../Attributes.md)中。在此示例中，它是 `Weight Tracker` 的子笔记 `Implementation`。该 Implementation 由两个[代码笔记](../../Note%20Types/Code.md)组成，分别包含一些 HTML 和 JavaScript，它们加载所有带有 `weight` 属性的笔记，并在图表中显示其值。

为了实际渲染图表，我们使用了一个名为 [chart.js](https://www.chartjs.org/) 的第三方库，它以附件形式导入，因为它并非 Trilium 内置的。

### 代码

以下是放置在类型为 `JS Frontend` 的[代码笔记](../../Note%20Types/Code.md)中的脚本内容：

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

在 `Weight Tracker` 的链接图中，有一个名为 `Button` 的笔记。打开它并删除或注释掉其内容。重启 Trilium 后，`Weight Tracker` 按钮将消失。