# 组件库

利用<a class="reference-link" href="../../Common%20concepts/Script%20bundles.md">脚本包</a>的概念，可以创建供多个小组件或<a class="reference-link" href="../../../Note%20Types/Render%20Note.md">渲染笔记</a>共享的组件。

## 导出单个组件

这对于大型组件通常非常有用。

以下是一个使用<a class="reference-link" href="../../../Note%20Types/Render%20Note.md">渲染笔记</a>的子层级示例：

*   _我的渲染笔记_  
    笔记类型：渲染笔记  
    将 `~renderNote` 链接到子笔记（_带有子组件的渲染笔记_）
    *   _带有子组件的渲染笔记_  
        类型：JSX
        
        ```jsx
        export default function() {
            return (
                <MyComponent />        
            );
        }
        ```
        
        *   _MyComponent_  
            类型：代码 / JSX
            
            ```jsx
            export default function MyComponent() {
                return <p>Hi</p>;
            }
            ```

## 每个笔记多个组件

要导出多个组件，请在每个函数组件旁边使用 `export` 关键字。

以下是一个名为 `MyComponents` 的子笔记的示例：

```jsx
export function MyFirstComponent() {
    return <p>First</p>;
}

export function MySecondComponent() {
    return <p>Bar</p>;
}
```

然后在它的父笔记中：

```jsx
const { MyFirstComponent, MySecondComponent } = MyComponents;

export default function() {
    return (
        <>
            <MyFirstComponent />
            <MySecondComponent />
        </>
    );
}
```

或者，也可以直接使用这些组件，而无需先将它们赋值给 `const`：

```jsx
<MyComponents.MyFirstComponent />
<MyComponents.MySecondComponent />
```