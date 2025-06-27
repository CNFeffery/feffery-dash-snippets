# feffery-dash-snippets: Dash 实用代码片段

简体中文 | [English](./README-en_US.md)

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

- `utils:i18n`: 快捷导入`feffery_dash_utils.i18n`中的`Translator`类

- `utils:dc`: 快捷导入`feffery_dash_utils.template_utils.dashboard_components`中全部的内置自定义组件

- `utils:version-check`: 快捷导入`feffery_dash_utils.version_utils`中的`check_python_version()`和`check_dependencies_version()`

#### 1.1.5 其他快捷片段

- `pic=`：快捷填入`prevent_initial_call=True`

- `adc=`：快捷填入`_allow_dynamic_callbacks=True`

- `run:debug`：快速创建`Dash`应用`debug`模式`if __name__ == '__main__':app.run(debug=True)`结构体

- `ad=`：快捷填入`allow_duplicate=True`

#### 1.1.6 快捷页面模板生成

- `template:basic_tool`：快捷生成单页面基础工具型应用模板

- `template:blank`：快捷生成最基础的空白应用模板

- `template:fact-jupyter`：快捷生成`fact`在`jupyter`中使用的模板

#### 1.1.7 常用配色方案快捷生成

- `colors:blues_3`：快速生成`blues_3`颜色值数组

- `colors:blues_4`：快速生成`blues_4`颜色值数组

- `colors:blues_5`：快速生成`blues_5`颜色值数组

- `colors:blues_6`：快速生成`blues_6`颜色值数组

- `colors:blues_7`：快速生成`blues_7`颜色值数组

- `colors:blues_8`：快速生成`blues_8`颜色值数组

- `colors:blues_9`：快速生成`blues_9`颜色值数组

- `colors:blues_3_r`：快速生成`blues_3_r`颜色值数组

- `colors:blues_4_r`：快速生成`blues_4_r`颜色值数组

- `colors:blues_5_r`：快速生成`blues_5_r`颜色值数组

- `colors:blues_6_r`：快速生成`blues_6_r`颜色值数组

- `colors:blues_7_r`：快速生成`blues_7_r`颜色值数组

- `colors:blues_8_r`：快速生成`blues_8_r`颜色值数组

- `colors:blues_9_r`：快速生成`blues_9_r`颜色值数组

- `colors:greens_3`：快速生成`greens_3`颜色值数组

- `colors:greens_4`：快速生成`greens_4`颜色值数组

- `colors:greens_5`：快速生成`greens_5`颜色值数组

- `colors:greens_6`：快速生成`greens_6`颜色值数组

- `colors:greens_7`：快速生成`greens_7`颜色值数组

- `colors:greens_8`：快速生成`greens_8`颜色值数组

- `colors:greens_9`：快速生成`greens_9`颜色值数组

- `colors:greens_3_r`：快速生成`greens_3_r`颜色值数组

- `colors:greens_4_r`：快速生成`greens_4_r`颜色值数组

- `colors:greens_5_r`：快速生成`greens_5_r`颜色值数组

- `colors:greens_6_r`：快速生成`greens_6_r`颜色值数组

- `colors:greens_7_r`：快速生成`greens_7_r`颜色值数组

- `colors:greens_8_r`：快速生成`greens_8_r`颜色值数组

- `colors:greens_9_r`：快速生成`greens_9_r`颜色值数组

- `colors:greys_3`：快速生成`greys_3`颜色值数组

- `colors:greys_4`：快速生成`greys_4`颜色值数组

- `colors:greys_5`：快速生成`greys_5`颜色值数组

- `colors:greys_6`：快速生成`greys_6`颜色值数组

- `colors:greys_7`：快速生成`greys_7`颜色值数组

- `colors:greys_8`：快速生成`greys_8`颜色值数组

- `colors:greys_9`：快速生成`greys_9`颜色值数组

- `colors:greys_3_r`：快速生成`greys_3_r`颜色值数组

- `colors:greys_4_r`：快速生成`greys_4_r`颜色值数组

- `colors:greys_5_r`：快速生成`greys_5_r`颜色值数组

- `colors:greys_6_r`：快速生成`greys_6_r`颜色值数组

- `colors:greys_7_r`：快速生成`greys_7_r`颜色值数组

- `colors:greys_8_r`：快速生成`greys_8_r`颜色值数组

- `colors:greys_9_r`：快速生成`greys_9_r`颜色值数组

- `colors:oranges_3`：快速生成`oranges_3`颜色值数组

- `colors:oranges_4`：快速生成`oranges_4`颜色值数组

- `colors:oranges_5`：快速生成`oranges_5`颜色值数组

- `colors:oranges_6`：快速生成`oranges_6`颜色值数组

- `colors:oranges_7`：快速生成`oranges_7`颜色值数组

- `colors:oranges_8`：快速生成`oranges_8`颜色值数组

- `colors:oranges_9`：快速生成`oranges_9`颜色值数组

- `colors:oranges_3_r`：快速生成`oranges_3_r`颜色值数组

- `colors:oranges_4_r`：快速生成`oranges_4_r`颜色值数组

- `colors:oranges_5_r`：快速生成`oranges_5_r`颜色值数组

- `colors:oranges_6_r`：快速生成`oranges_6_r`颜色值数组

- `colors:oranges_7_r`：快速生成`oranges_7_r`颜色值数组

- `colors:oranges_8_r`：快速生成`oranges_8_r`颜色值数组

- `colors:oranges_9_r`：快速生成`oranges_9_r`颜色值数组

- `colors:purples_3`：快速生成`purples_3`颜色值数组

- `colors:purples_4`：快速生成`purples_4`颜色值数组

- `colors:purples_5`：快速生成`purples_5`颜色值数组

- `colors:purples_6`：快速生成`purples_6`颜色值数组

- `colors:purples_7`：快速生成`purples_7`颜色值数组

- `colors:purples_8`：快速生成`purples_8`颜色值数组

- `colors:purples_9`：快速生成`purples_9`颜色值数组

- `colors:purples_3_r`：快速生成`purples_3_r`颜色值数组

- `colors:purples_4_r`：快速生成`purples_4_r`颜色值数组

- `colors:purples_5_r`：快速生成`purples_5_r`颜色值数组

- `colors:purples_6_r`：快速生成`purples_6_r`颜色值数组

- `colors:purples_7_r`：快速生成`purples_7_r`颜色值数组

- `colors:purples_8_r`：快速生成`purples_8_r`颜色值数组

- `colors:purples_9_r`：快速生成`purples_9_r`颜色值数组

- `colors:reds_3`：快速生成`reds_3`颜色值数组

- `colors:reds_4`：快速生成`reds_4`颜色值数组

- `colors:reds_5`：快速生成`reds_5`颜色值数组

- `colors:reds_6`：快速生成`reds_6`颜色值数组

- `colors:reds_7`：快速生成`reds_7`颜色值数组

- `colors:reds_8`：快速生成`reds_8`颜色值数组

- `colors:reds_9`：快速生成`reds_9`颜色值数组

- `colors:reds_3_r`：快速生成`reds_3_r`颜色值数组

- `colors:reds_4_r`：快速生成`reds_4_r`颜色值数组

- `colors:reds_5_r`：快速生成`reds_5_r`颜色值数组

- `colors:reds_6_r`：快速生成`reds_6_r`颜色值数组

- `colors:reds_7_r`：快速生成`reds_7_r`颜色值数组

- `colors:reds_8_r`：快速生成`reds_8_r`颜色值数组

- `colors:reds_9_r`：快速生成`reds_9_r`颜色值数组

### 1.2 快捷 JavaScript 代码片段

#### 1.2.1 回调相关快捷逻辑初始化

- `callback:init`：快捷生成浏览器端回调函数定义模板

- `callback:no_update`：快捷插入浏览器端回调版本的`dash.no_update`

- `callback:PreventUpdate`：快捷插入浏览器端回调版本的`PreventUpdate`

- `callback:ctx`：快捷插入浏览器端回调版本的`dash.ctx`

- `callback:set_props`：快捷插入浏览器端回调版本的`set_props()`

- `callback:triggered`：快捷插入浏览器端回调版本的`dash.ctx.triggered`

- `callback:triggered_id`：快捷插入浏览器端回调版本的`dash.ctx.triggered_id`

- `callback:inputs_list`：快捷插入浏览器端回调版本的`dash.ctx.inputs_list`

- `callback:inputs`：快捷插入浏览器端回调版本的`dash.ctx.inputs`

- `callback:states_list`：快捷插入浏览器端回调版本的`dash.ctx.states_list`

- `callback:states`：快捷插入浏览器端回调版本的`dash.ctx.states`

- `callback:outputs_list`：快捷插入浏览器端回调版本的`dash.ctx.outputs_list`

### 1.3 快捷 CSS 代码片段

- `css>scrollbar`：快捷构建兼容各主流浏览器的`滚动条美化`策略

- `css>init-loading`：快捷构建`dash`应用自定义`初始加载动画策略`

### 1.4 快捷 JSON 代码片段

- `locales`：在`JSON`数据中快捷生成`feffery_dash_utils.i18n.Translator`对应的本地国际化配置模板
