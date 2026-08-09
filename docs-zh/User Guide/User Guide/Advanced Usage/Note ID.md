# 笔记 ID

有些应用程序使用文件名来唯一标识笔记，而 Trilium 则采用笔记 ID 的概念。

通常，笔记 ID 是一个 12 字符长的字母数字序列（包含大小写字母），为每个新笔记随机生成。

## 导入/导出如何影响笔记 ID

当笔记被导出时，其笔记 ID 会保留在导出的元数据中。然而，当它们被重新导入时，所有笔记都会生成新的笔记 ID。这也包括导入/导出过程中涉及的其他实体，例如 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>。

## 笔记冲突

由于笔记 ID 是固定宽度的随机生成数字，根据[鸽笼原理](https://en.wikipedia.org/wiki/Pigeonhole_principle)，新创建的笔记有可能与现有笔记拥有相同的 ID。

由于笔记 ID 是字母数字且长度为 12，我们有 $62^{12}$ 个唯一 ID。然而，由于我们是随机生成的，我们可以使用类似 [Nano ID](https://alex7kom.github.io/nano-nanoid-cc/?alphabet=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz&size=12&speed=1000&speedUnit=hour) 的冲突计算器来确定，我们需要每小时创建 1000 个笔记，持续 9 个世纪，才能有至少 1% 的笔记冲突概率。

因此，Trilium 不会针对潜在的笔记冲突采取任何明确措施，这与使用唯一哈希的其他软件（如 [Git](https://stackoverflow.com/questions/10434326/hash-collision-in-git)）类似。如果理论上发生冲突，最可能的情况是现有笔记将被新笔记替换。