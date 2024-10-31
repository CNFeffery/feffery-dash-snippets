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

#### 1.1.5 Other Quick Snippets

- `pic=`: Quickly fill in `prevent_initial_call=True`

- `run:debug`: Quickly create a `Dash` app in `debug` mode with the structure `if __name__ == '__main__': app.run(debug=True)`

- `ad=`: Quickly fill in `allow_duplicate=True`

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
