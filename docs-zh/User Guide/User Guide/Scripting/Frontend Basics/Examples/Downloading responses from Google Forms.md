# 从 Google 表单下载回复

本教程展示了与 Google 表单的基本集成，我们可以使用“关联到表格”功能下载表单的回复。

请注意，该链接将对所有人公开可访问（不过链接格式难以猜测，例如 `https://docs.google.com/spreadsheets/d/e/2PACX-1vTA8NU2_eZFhc8TFadCZPreBfvP7un8IHd6J0SchrLLw3ueGmntNZjwRmsH2ZRcp1pJYDAzMz1FmFaj/pub?output=csv`）。请确保您不会意外发布敏感信息。

## 获取 CSV 链接

1.  在浏览器中打开 Google 表单。
2.  选择“回复”选项卡，然后点击“关联到表格”。
3.  选择“创建新电子表格”，然后按“创建”。
4.  在 Google 表格中，选择 文件 → 共享 → 发布到网络。
5.  在“发布到网络”界面中，确保选中“链接”选项卡，并将“网页”改为“逗号分隔值 (.csv)”。
6.  复制提供的链接，该链接将用于接下来的脚本。

## 创建脚本

创建一个“JS 前端”脚本：

```
const CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTiwooLV2whjCSVa49dJ99p_G3_qhqHHRqttMjYCJVfLXVdTgUSNJu5K0rpqmaHYF2k7Vofi3o7gW82/pub?output=csv";

async function fetchData() {
    try {
        const response = await fetch(CSV_URL);
        return await response.text();
    } catch (e) {
        api.showError(e.message);
    }
}

const data = await fetchData();
console.log(data);
// 对数据执行某些操作。
```

请注意，数据将以字符串形式接收，并且没有库可供我们进行 CSV 解析。要进行非常简单的 CSV 解析：

```
const content = data
	.split("\n")
	.slice(1)
	.map((row) => row.split(","));
```

这将把数据作为数组的数组返回。