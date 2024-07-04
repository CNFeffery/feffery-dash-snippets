# feffery-dash-snippets: Dash 实用代码片段

![](https://raw.githubusercontent.com/CNFeffery/feffery-dash-snippets/main/assets/demo.gif)

## 1 快捷代码片段

### 1.1 快捷 Python 代码片段

#### 1.1.1 快捷模块功能导入

- `ihd`：从`dash`快捷导入`html`、`dcc`

- `ibcr`：从`dash`快捷导入基础回调角色`Input`、`Output`、`State`

- `ifac`：快捷导入`feffery_antd_components`（`fac`）

- `ifuc`：快捷导入`feffery_utils_components`（`fuc`）

- `ifact`：快捷导入`feffery_antd_charts`（`fact`）

- `ifmc`：快捷导入`feffery_markdown_components`（`fmc`）

- `iflc`：快捷导入`feffery_leaflet_components`（`flc`）

- `ifm`：快捷导入`feffery_maplibre`（`fm`）

- `ifamc`：快捷导入`feffery_antd_mobile_components`（`famc`）

#### 1.1.2 flask 相关快捷逻辑初始化

- `flask:upload`：快速初始化`flask`上传服务接口

- `flask:download`：快速初始化`flask`下载服务接口

- `flask:stream`：快速初始化`flask`流式服务（SSE）接口

#### 1.1.3 回调相关快捷逻辑初始化

- `callback:oi`：快速初始化具有`Input`和`Output`角色的回调函数

- `callback:ois`：快速初始化具有`Input`、`Output`及`State`角色的回调函数

- `callback-cs:oi`：快速初始化具有`Input`和`Output`角色的浏览器端回调函数

- `callback-cs:ois`：快速初始化具有`Input`、`Output`及`State`角色的浏览器端回调函数

#### 1.1.4 feffery-dash-utils 工具函数快捷导入

- `utils:style`: 快捷导入`feffery_dash_utils.style_utils`中的`style()`函数

- `utils:tm`: 快捷导入`feffery_dash_utils.tree_utils`中的`TreeManager`类

#### 1.1.5 其他快捷片段

- `pic=`：快捷填入`prevent_initial_call=True`

- `run:debug`：快速创建`Dash`应用`debug`模式`if __name__ == '__main__':app.run(debug=True)`结构体

- `ad=`：快捷填入`allow_duplicate=True`

### 1.2 快捷 JavaScript 代码片段

#### 1.2.1 回调相关快捷逻辑初始化

- `callback:init`：快捷生成浏览器端回调函数定义模板

- `dash.no_update`：快捷插入浏览器端回调版本的`dash.no_update`

- `PreventUpdate`：快捷插入浏览器端回调版本的`dash.PreventUpdate`

- `dash.callback_context`：快捷插入浏览器端回调版本的`dash.callback_context`

- `set_props`: 快捷插入浏览器端回调版本的`dash.set_props()`

### 1.3 快捷 CSS 代码片段

- `css>scrollbar`：快捷构建兼容各主流浏览器的`滚动条美化`策略

- `css>init-loading`：快捷构建`dash`应用自定义`初始加载动画策略`
