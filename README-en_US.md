# feffery-dash-snippets: Practical Dash Code Snippets

[简体中文](./README.md) | English

![](https://raw.githubusercontent.com/CNFeffery/feffery-dash-snippets/main/assets/demo.gif)

## 1 Quick Code Snippets

### 1.1 Quick Python Code Snippets

#### 1.1.1 Quick Module Functionality Import

- `ihd`: Quickly import `html`, `dcc` from `dash`

- `ibcr`: Quickly import basic callback roles `Input`, `Output`, `State` from `dash`

- `ifac`: Quickly import `feffery_antd_components` (alias `fac`)

- `ifuc`: Quickly import `feffery_utils_components` (alias `fuc`)

- `ifact`: Quickly import `feffery_antd_charts` (alias `fact`)

- `ifmc`: Quickly import `feffery_markdown_components` (alias `fmc`)

- `iflc`: Quickly import `feffery_leaflet_components` (alias `flc`)

- `ifm`: Quickly import `feffery_maplibre` (alias `fm`)

- `ifamc`: Quickly import `feffery_antd_mobile_components` (alias `famc`)

#### 1.1.2 Flask-Related Quick Logic Initialization

- `flask:upload`: Quickly initialize Flask upload service interface

- `flask:download`: Quickly initialize Flask download service interface

- `flask:stream`: Quickly initialize Flask streaming service (SSE) interface

#### 1.1.3 Callback-Related Quick Logic Initialization

- `callback:oi`: Quickly initialize a callback function with `Input` and `Output` roles

- `callback:ois`: Quickly initialize a callback function with `Input`, `Output`, and `State` roles

- `callback-cs:oi`: Quickly initialize a client-side callback function with `Input` and `Output` roles

- `callback-cs:ois`: Quickly initialize a client-side callback function with `Input`, `Output`, and `State` roles

#### 1.1.4 Quick Import of feffery-dash-utils Utility Functions

- `utils:style`: Quickly import the `style()` function from `feffery_dash_utils.style_utils`

- `utils:tm`: Quickly import the `TreeManager` class from `feffery_dash_utils.tree_utils`

- `utils:i18n`: Quickly import the `Translator` class from `feffery_dash_utils.i18n`

- `utils:dc`: Quickly import all built-in custom components in `feffery_dash_utils.template_utils.dashboard_components`

- `utils:version-check`: Quickly import the `check_python_version()` and `check_dependencies_version()` functions from `feffery_dash_utils.version_utils`

#### 1.1.5 Other Quick Snippets

- `pic=`: Quickly fill in `prevent_initial_call=True`

- `run:debug`: Quickly create a `Dash` app in `debug` mode with the structure `if __name__ == '__main__': app.run(debug=True)`

- `ad=`: Quickly fill in `allow_duplicate=True`

#### 1.1.6 Quick Page Template Generation

- `template:basic_tool`: Quickly generate a single-page basic tool-type app

- `template:blank`: Quickly generate a basic blank application template

- `template:fact-jupyter`：Quickly generate `fact` template which is run in `jupyter`

#### 1.1.7 Quick Generation of Common Color Schemes

- `colors:blues_3`: Quickly generate the `blues_3` color value array

- `colors:blues_4`: Quickly generate the `blues_4` color value array

- `colors:blues_5`: Quickly generate the `blues_5` color value array

- `colors:blues_6`: Quickly generate the `blues_6` color value array

- `colors:blues_7`: Quickly generate the `blues_7` color value array

- `colors:blues_8`: Quickly generate the `blues_8` color value array

- `colors:blues_9`: Quickly generate the `blues_9` color value array

- `colors:blues_3_r`: Quickly generate the `blues_3_r` color value array

- `colors:blues_4_r`: Quickly generate the `blues_4_r` color value array

- `colors:blues_5_r`: Quickly generate the `blues_5_r` color value array

- `colors:blues_6_r`: Quickly generate the `blues_6_r` color value array

- `colors:blues_7_r`: Quickly generate the `blues_7_r` color value array

- `colors:blues_8_r`: Quickly generate the `blues_8_r` color value array

- `colors:blues_9_r`: Quickly generate the `blues_9_r` color value array

- `colors:greens_3`: Quickly generate the `greens_3` color value array

- `colors:greens_4`: Quickly generate the `greens_4` color value array

- `colors:greens_5`: Quickly generate the `greens_5` color value array

- `colors:greens_6`: Quickly generate the `greens_6` color value array

- `colors:greens_7`: Quickly generate the `greens_7` color value array

- `colors:greens_8`: Quickly generate the `greens_8` color value array

- `colors:greens_9`: Quickly generate the `greens_9` color value array

- `colors:greens_3_r`: Quickly generate the `greens_3_r` color value array

- `colors:greens_4_r`: Quickly generate the `greens_4_r` color value array

- `colors:greens_5_r`: Quickly generate the `greens_5_r` color value array

- `colors:greens_6_r`: Quickly generate the `greens_6_r` color value array

- `colors:greens_7_r`: Quickly generate the `greens_7_r` color value array

- `colors:greens_8_r`: Quickly generate the `greens_8_r` color value array

- `colors:greens_9_r`: Quickly generate the `greens_9_r` color value array

- `colors:greys_3`: Quickly generate the `greys_3` color value array

- `colors:greys_4`: Quickly generate the `greys_4` color value array

- `colors:greys_5`: Quickly generate the `greys_5` color value array

- `colors:greys_6`: Quickly generate the `greys_6` color value array

- `colors:greys_7`: Quickly generate the `greys_7` color value array

- `colors:greys_8`: Quickly generate the `greys_8` color value array

- `colors:greys_9`: Quickly generate the `greys_9` color value array

- `colors:greys_3_r`: Quickly generate the `greys_3_r` color value array

- `colors:greys_4_r`: Quickly generate the `greys_4_r` color value array

- `colors:greys_5_r`: Quickly generate the `greys_5_r` color value array

- `colors:greys_6_r`: Quickly generate the `greys_6_r` color value array

- `colors:greys_7_r`: Quickly generate the `greys_7_r` color value array

- `colors:greys_8_r`: Quickly generate the `greys_8_r` color value array

- `colors:greys_9_r`: Quickly generate the `greys_9_r` color value array

- `colors:oranges_3`: Quickly generate the `oranges_3` color value array

- `colors:oranges_4`: Quickly generate the `oranges_4` color value array

- `colors:oranges_5`: Quickly generate the `oranges_5` color value array

- `colors:oranges_6`: Quickly generate the `oranges_6` color value array

- `colors:oranges_7`: Quickly generate the `oranges_7` color value array

- `colors:oranges_8`: Quickly generate the `oranges_8` color value array

- `colors:oranges_9`: Quickly generate the `oranges_9` color value array

- `colors:oranges_3_r`: Quickly generate the `oranges_3_r` color value array

- `colors:oranges_4_r`: Quickly generate the `oranges_4_r` color value array

- `colors:oranges_5_r`: Quickly generate the `oranges_5_r` color value array

- `colors:oranges_6_r`: Quickly generate the `oranges_6_r` color value array

- `colors:oranges_7_r`: Quickly generate the `oranges_7_r` color value array

- `colors:oranges_8_r`: Quickly generate the `oranges_8_r` color value array

- `colors:oranges_9_r`: Quickly generate the `oranges_9_r` color value array

- `colors:purples_3`: Quickly generate the `purples_3` color value array

- `colors:purples_4`: Quickly generate the `purples_4` color value array

- `colors:purples_5`: Quickly generate the `purples_5` color value array

- `colors:purples_6`: Quickly generate the `purples_6` color value array

- `colors:purples_7`: Quickly generate the `purples_7` color value array

- `colors:purples_8`: Quickly generate the `purples_8` color value array

- `colors:purples_9`: Quickly generate the `purples_9` color value array

- `colors:purples_3_r`: Quickly generate the `purples_3_r` color value array

- `colors:purples_4_r`: Quickly generate the `purples_4_r` color value array

- `colors:purples_5_r`: Quickly generate the `purples_5_r` color value array

- `colors:purples_6_r`: Quickly generate the `purples_6_r` color value array

- `colors:purples_7_r`: Quickly generate the `purples_7_r` color value array

- `colors:purples_8_r`: Quickly generate the `purples_8_r` color value array

- `colors:purples_9_r`: Quickly generate the `purples_9_r` color value array

- `colors:reds_3`: Quickly generate the `reds_3` color value array

- `colors:reds_4`: Quickly generate the `reds_4` color value array

- `colors:reds_5`: Quickly generate the `reds_5` color value array

- `colors:reds_6`: Quickly generate the `reds_6` color value array

- `colors:reds_7`: Quickly generate the `reds_7` color value array

- `colors:reds_8`: Quickly generate the `reds_8` color value array

- `colors:reds_9`: Quickly generate the `reds_9` color value array

- `colors:reds_3_r`: Quickly generate the `reds_3_r` color value array

- `colors:reds_4_r`: Quickly generate the `reds_4_r` color value array

- `colors:reds_5_r`: Quickly generate the `reds_5_r` color value array

- `colors:reds_6_r`: Quickly generate the `reds_6_r` color value array

- `colors:reds_7_r`: Quickly generate the `reds_7_r` color value array

- `colors:reds_8_r`: Quickly generate the `reds_8_r` color value array

- `colors:reds_9_r`: Quickly generate the `reds_9_r` color value array

### 1.2 Quick JavaScript Code Snippets

#### 1.2.1 Callback-Related Quick Logic Initialization

- `callback:init`: Quickly generate a template for defining callback functions on the browser side.

- `callback:no_update`: Quickly insert the browser-side callback version of `dash.no_update`.

- `callback:PreventUpdate`: Quickly insert the browser-side callback version of `PreventUpdate`.

- `callback:ctx`: Quickly insert the browser-side callback version of `dash.ctx`.

- `callback:set_props`: Quickly insert the browser-side callback version of `set_props()`.

- `callback:triggered`: Quickly insert the browser-side callback version of `dash.ctx.triggered`.

- `callback:triggered_id`: Quickly insert the browser-side callback version of `dash.ctx.triggered_id`.

- `callback:inputs_list`: Quickly insert the browser-side callback version of `dash.ctx.inputs_list`.

- `callback:inputs`: Quickly insert the browser-side callback version of `dash.ctx.inputs`.

- `callback:states_list`: Quickly insert the browser-side callback version of `dash.ctx.states_list`.

- `callback:states`: Quickly insert the browser-side callback version of `dash.ctx.states`.

- `callback:outputs_list`: Quickly insert the browser-side callback version of `dash.ctx.outputs_list`.

### 1.3 Quick CSS Code Snippets

- `css>scrollbar`: Quickly construct a `scrollbar beautification` strategy compatible with major browsers

- `css>init-loading`: Quickly construct a custom `initial loading animation strategy` for `dash` apps

### 1.4 Quick JSON Code Snippets

- `locales`: Quickly generate a local internationalization configuration template corresponding to `feffery_dash_utils.i18n.Translator` in `JSON` data
