# feffery-dash-snippets: Dash 实用代码片段

![](https://raw.githubusercontent.com/CNFeffery/feffery-dash-snippets/main/assets/demo.gif)

## 1 快捷代码片段

### 1.1 快捷Python代码片段

#### 1.1.1 快捷模块功能导入

- *`ihd`*：从`dash`快捷导入`html`、`dcc`

- *`ibcr`*：从`dash`快捷导入基础回调角色`Input`、`Output`、`State`

- *`ifac`*：快捷导入`feffery_antd_components`（`fac`）

- *`ifuc`*：快捷导入`feffery_utils_components`（`fuc`）

- *`ifact`*：快捷导入`feffery_antd_charts`（`fact`）

- *`ifmc`*：快捷导入`feffery_markdown_components`（`fmc`）

- *`iflc`*：快捷导入`feffery_leaflet_components`（`flc`）

#### 1.1.2 flask 相关快捷逻辑初始化

- *`flask:upload`*：快速初始化`flask`上传服务接口

- *`flask:download`*：快速初始化`flask`下载服务接口

#### 1.1.3 回调相关快捷逻辑初始化

- *`callback:oi`*：快速初始化具有`Input`和`Output`角色的回调函数

- *`callback:ois`*：快速初始化具有`Input`、`Output`及`State`角色的回调函数

- *`callback-cs:oi`*：快速初始化具有`Input`和`Output`角色的浏览器端回调函数

- *`callback-cs:ois`*：快速初始化具有`Input`、`Output`及`State`角色的浏览器端回调函数

#### 1.1.4 其他快捷片段

- *`pic=`*：快捷填入`prevent_initial_call=True`

### 1.2 快捷Javascript代码片段

#### 1.2.1 回调相关快捷逻辑初始化

- *`callback:init`*：快捷生成浏览器端回调函数定义模板

- *`dash.no_update`*：快捷插入浏览器端回调版本的`dash.no_update`

- *`PreventUpdate`*：快捷插入浏览器端回调版本的`dash.PreventUpdate`

- *`dash.callback_context`*：快捷插入浏览器端回调版本的`dash.callback_context`

### 1.3 快捷Css代码片段

- *`css>scrollbar`*：快捷构建兼容各主流浏览器的`滚动条美化`策略

- *`css>init-loading`*：快捷构建`dash`应用自定义`初始加载动画策略`