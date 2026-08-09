# 脚本捆绑包

对于<a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a>和更复杂的脚本，通常将代码拆分为多个<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记是很有用的。

当脚本运行时，会检查正在运行的脚本（或<a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a>）的子笔记。如果这些子笔记是与所运行代码类型（前端或后端）相对应的代码笔记，它们也会被一并求值。

一个脚本及其子笔记的集合称为_捆绑包_。捆绑包中的子笔记称为_模块_。

作为依赖关系的基本示例，请考虑以下笔记结构：

*   _带依赖的脚本_
    
    ```javascript
    api.log(MyMath.sum(2, 2));
    ```
    
    *   _MyMath_
        
        ```javascript
        module.exports = {
            sum(a, b) {
                return a + b;
            }
        };
        ```

当运行_带依赖的脚本_时，它会检测到_MyMath_作为子模块，并将其`module.exports`对象的结果提供到一个与笔记同名的全局对象中。

> [!NOTE]
> 如果笔记名称包含空格或特殊字符，这些字符将被移除。例如`My Nice Note!`会变成`MyNiceNote`。

## 替代语法

除了向`module.exports`提供一个对象，也可以逐个添加字段：

```javascript
module.exports.sum = (a, b) => a + b;
module.exports.subtract = (a, b) => a - b;
```

## 从捆绑包中忽略代码脚本

要忽略某个脚本使其不包含在捆绑包中（例如，如果它与父脚本笔记无关），请应用`#disableInclusion`标签。

## 在多个捆绑包之间共享模块

可以通过在两个模块之间简单地克隆共享模块来在多个脚本之间重用模块（参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Cloning%20Notes.md">克隆笔记</a>）。

可选地，可以使用一个单独的笔记来包含所有不同的可重用模块，以便于发现它们。