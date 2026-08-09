# 演示文档

演示文档是一个导出的 .zip 文件，位于 `apps/server/src/assets/db/demo.zip`。

在引导过程中，如果用户选择他们是新用户，则 `demo.zip` 会被导入到根笔记中。

## 修改文档

1.  在 Git 根目录下，运行 `pnpm edit-docs:edit-demo`。
2.  等待桌面应用显示文档。
3.  直接进行所需的修改。
4.  等待几秒钟，让更改在后台处理。
5.  在 Git 中提交更改。

## 测试更改

1.  运行：
    
    ```
    rm -r data
    pnpm server:start
    ```
2.  然后重新进行引导。