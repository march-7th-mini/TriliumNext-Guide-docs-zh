```markdown
import {
    ActionButton, Button, LinkButton,
    Admonition, Collapsible,
    FormCheckbox, FormDropdownList, FormFileUploadButton, FormGroup, FormRadioGroup, FormTextArea,
    FormTextBox, FormToggle, Slider, RawHtml, LoadingSpinner, Icon,
    ColorPicker,
    Dropdown, FormListItem, FormDropdownDivider, FormDropdownSubmenu,
    NoteAutocomplete, NoteLink, Modal,
    Table,
    CKEditor,
    useEffect, useState
} from "trilium:preact";
import { showMessage } from "trilium:api";

export default function() {
    const [ time, setTime ] = useState();
    const lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam accumsan eu odio non gravida. Pellentesque ornare, arcu condimentum molestie dignissim, nibh turpis ultrices elit, eget elementum nunc erat at erat. Maecenas vehicula consectetur elit, nec fermentum elit venenatis eu.";
    useEffect(() => {
        const interval = setInterval(() => setTime(new Date().toLocaleString()), 1000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div style={{ padding: 20, display: "flex", flexDirection: "column", gap: "1em" }}>
            <h1>小组件展示</h1>

            <Buttons />
            <Admonition type="note">
                <strong>警示框</strong><br />
                {lorem}
            </Admonition>

            <Collapsible title="可折叠区域" initiallyExpanded>
                {lorem}
            </Collapsible>

            <FormElements />
            <NoteElements />
            <ModalSample />
            <DropdownSample />
            <CollectionViews />
        </div>
    );
}

function Buttons() {
    const onClick = () => showMessage("按下了按钮");

    return (
        <>
            <h2>按钮</h2>
            <div style={{ display: "flex", gap: "1em", alignItems: "center" }}>
                <ActionButton icon="bx bx-rocket" text="操作按钮" onClick={onClick} />
                <Button icon="bx bx-rocket" text="简单按钮" onClick={onClick} />
                <LinkButton text="链接按钮" onClick={onClick} />
            </div>
        </>
    )
}

function FormElements() {
    const [ checkboxChecked, setCheckboxChecked ] = useState(false);
    const [ dropdownValue, setDropdownValue ] = useState("key-1");
    const [ radioGroupValue, setRadioGroupValue ] = useState("key-1");
    const [ sliderValue, setSliderValue ] = useState(50);
    const [ color, setColor ] = useState("#43a047");

    return (
        <>
            <h2>表单元素</h2>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: "1em" }}>
                <FormGroup name="checkbox" label="复选框">
                    <FormCheckbox label="复选框" currentValue={checkboxChecked} onChange={setCheckboxChecked} />
                </FormGroup>
                <FormGroup name="toggle" label="开关">
                    <FormToggle switchOnName="关" switchOffName="开" currentValue={checkboxChecked} onChange={setCheckboxChecked} />
                </FormGroup>
                <FormGroup name="dropdown" label="下拉列表">
                    <FormDropdownList
                        values={[
                            { key: "key-1", name: "第一项" },
                            { key: "key-2", name: "第二项" },
                            { key: "key-3", name: "第三项" },
                        ]}
                        currentValue={dropdownValue} onChange={setDropdownValue}
                        keyProperty="key" titleProperty="name"
                    />
                </FormGroup>
                <FormGroup name="radio-group" label="单选组">
                    <FormRadioGroup
                        values={[
                            { value: "key-1", label: "第一项" },
                            { value: "key-2", label: "第二项" },
                            { value: "key-3", label: "第三项" },
                        ]}
                        currentValue={radioGroupValue} onChange={setRadioGroupValue}
                    />
                </FormGroup>
                <FormGroup name="text-box" label="文本框">
                    <FormTextBox
                        placeholder="输入一些内容..."
                        currentValue="" onChange={(newValue) => {}}
                    />
                </FormGroup>
                <FormGroup name="text-area" label="文本区域">
                    <FormTextArea
                        placeholder="输入更多内容..."
                        currentValue="" onChange={(newValue) => {}}
                    />
                </FormGroup>
                <FormGroup name="color-picker" label="颜色选择器">
                    <ColorPicker currentValue={color} onChange={setColor} />
                </FormGroup>
                <FormGroup name="slider" label="滑块">
                    <Slider
                        min={1} max={100}
                        value={sliderValue} onChange={setSliderValue}
                    />
                </FormGroup>
                <FormGroup name="file-upload" label="文件上传">
                    <FormFileUploadButton
                        text="上传"
                        onChange={(files) => {
                            const file = files?.[0];
                            if (!file) return;
                            showMessage(`获取到文件 "${file.name}"，大小为 ${file.size} 字节，类型为 ${file.type}。`);
                        }}
                    />
                </FormGroup>
                <FormGroup name="icon" label="图标">
                    <Icon icon="bx bx-smile" />
                </FormGroup>
                <FormGroup name="loading-spinner" label="加载指示器">
                    <LoadingSpinner />
                </FormGroup>
                <FormGroup name="raw-html" label="原始 HTML">
                    <RawHtml html="<strong>你好</strong> <em>世界</em>" />
                </FormGroup>
            </div>
        </>
    )
}

function NoteElements() {
    const [ noteId, setNoteId ] = useState("");

    return (
        <div>
            <h2>笔记元素</h2>

            <FormGroup name="note-autocomplete" label="笔记自动完成">
                <NoteAutocomplete
                    placeholder="选择一个笔记"
                    noteId={noteId} noteIdChanged={setNoteId}
                />
            </FormGroup>

            <FormGroup name="note-link" label="笔记链接">
                {noteId
                ? <NoteLink notePath={noteId} showNoteIcon />
                : <span>请先选择一个笔记</span>}
            </FormGroup>
        </div>
    );
}

function ModalSample() {
    const [ shown, setShown ] = useState(false);

    return (
        <>
            <h2>模态框</h2>
            <Button text="打开模态框" onClick={() => setShown(true)} />
            <Modal title="模态框标题" size="md" show={shown} onHidden={() => setShown(false)}>
                模态框内容显示在这里。
            </Modal>
        </>
    )
}

function DropdownSample() {
    return (
        <>
            <h2>下拉菜单</h2>
            <Dropdown text="下拉菜单" hideToggleArrow>
                <FormListItem icon="bx bx-cut">剪切</FormListItem>
                <FormListItem icon="bx bx-copy">复制</FormListItem>
                <FormListItem icon="bx bx-paste">粘贴</FormListItem>
                <FormDropdownDivider />
                <FormDropdownSubmenu title="子菜单">
                    <FormListItem>更多项目</FormListItem>
                </FormDropdownSubmenu>
            </Dropdown>
        </>
    )
}

function CollectionViews() {
    return (
        <>
            <h2>集合视图</h2>
            <p>
                提供了一个通用的 <code>Table</code> (Tabulator) 组件。同时也提供了 <code>Calendar</code>
                {" "}(FullCalendar) 组件，但它需要你传入一个 <code>plugins</code> 数组来渲染视图，因此这里不做演示。
            </p>
            <Table
                layout="fitColumns"
                columns={[
                    { title: "名称", field: "name" },
                    { title: "进度", field: "progress" }
                ]}
                data={[
                    { id: 1, name: "第一个任务", progress: "80%" },
                    { id: 2, name: "第二个任务", progress: "20%" }
                ]}
            />
        </>
    )
}
```