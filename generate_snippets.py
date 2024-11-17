import json

raw_snippets = [
    {
        'name': 'server-side-snippets',
        'language': 'python',
        'items': [
            {
                'title': 'import html, dcc from dash',
                'prefix': 'ihd',
                'description': 'Code snippet to import html and dcc from dash',
                'body_path': r'raw_snippets\py\ihd.py',
            },
            {
                'title': 'import basic callback roles',
                'prefix': 'ibcr',
                'description': 'Code snippet to import basic callback roles from dash',
                'body_path': r'raw_snippets\py\ibcr.py',
            },
            {
                'title': 'import fac',
                'prefix': 'ifac',
                'description': 'Code snippet to import fac',
                'body_path': r'raw_snippets\py\ifac.py',
            },
            {
                'title': 'import fuc',
                'prefix': 'ifuc',
                'description': 'Code snippet to import fuc',
                'body_path': r'raw_snippets\py\ifuc.py',
            },
            {
                'title': 'import fact',
                'prefix': 'ifact',
                'description': 'Code snippet to import fact',
                'body_path': r'raw_snippets\py\ifact.py',
            },
            {
                'title': 'import fmc',
                'prefix': 'ifmc',
                'description': 'Code snippet to import fmc',
                'body_path': r'raw_snippets\py\ifmc.py',
            },
            {
                'title': 'import flc',
                'prefix': 'iflc',
                'description': 'Code snippet to import flc',
                'body_path': r'raw_snippets\py\iflc.py',
            },
            {
                'title': 'import fm',
                'prefix': 'ifm',
                'description': 'Code snippet to import fm',
                'body_path': r'raw_snippets\py\ifm.py',
            },
            {
                'title': 'import famc',
                'prefix': 'ifamc',
                'description': 'Code snippet to import famc',
                'body_path': r'raw_snippets\py\ifamc.py',
            },
            {
                'title': 'quickly create flask upload api',
                'prefix': 'flask:upload',
                'description': 'Code snippet to quickly create flask upload api template',
                'body_path': r'raw_snippets\py\flask_upload.py',
            },
            {
                'title': 'quickly create flask download api',
                'prefix': 'flask:download',
                'description': 'Code snippet to quickly create flask download api template',
                'body_path': r'raw_snippets\py\flask_download.py',
            },
            {
                'title': 'quickly create flask stream api',
                'prefix': 'flask:stream',
                'description': 'Code snippet to quickly create flask stream(sse) api template',
                'body_path': r'raw_snippets\py\flask_stream.py',
            },
            {
                'title': 'quickly create callback without state',
                'prefix': 'callback:oi',
                'description': 'Code snippet to quickly create callback without state',
                'body_path': r'raw_snippets\py\callback_oi.py',
            },
            {
                'title': 'quickly create callback with state',
                'prefix': 'callback:ois',
                'description': 'Code snippet to quickly create callback with state',
                'body_path': r'raw_snippets\py\callback_ois.py',
            },
            {
                'title': 'quickly create client side callback without state',
                'prefix': 'callback-cs:oi',
                'description': 'Code snippet to quickly create client side callback without state',
                'body_path': r'raw_snippets\py\callback_cs_oi.py',
            },
            {
                'title': 'quickly create client side callback with state',
                'prefix': 'callback-cs:ois',
                'description': 'Code snippet to quickly create client side callback with state',
                'body_path': r'raw_snippets\py\callback_cs_ois.py',
            },
            {
                'title': 'set prevent_initial_call=True',
                'prefix': 'pic=',
                'description': 'Code snippet to add prevent_initial_call=True',
                'body_path': r'raw_snippets\py\prevent_initial_call.py',
            },
            {
                'title': 'generate dash debug mode run() structure',
                'prefix': 'run:debug',
                'description': 'generate dash debug mode run() structure',
                'body_path': r'raw_snippets\py\run_debug.py',
            },
            {
                'title': 'set allow_duplicate=True',
                'prefix': 'ad=',
                'description': 'Code snippet to add allow_duplicate=True',
                'body_path': r'raw_snippets\py\allow_duplicate.py',
            },
            {
                'title': 'quickly import style() from feffery-dash-utils',
                'prefix': 'utils:style',
                'description': 'Code snippet to import style() from feffery-dash-utils quickly',
                'body_path': r'raw_snippets\py\utils_style.py',
            },
            {
                'title': 'quickly import TreeManager from feffery-dash-utils',
                'prefix': 'utils:tm',
                'description': 'Code snippet to import TreeManager from feffery-dash-utils quickly',
                'body_path': r'raw_snippets\py\utils_tm.py',
            },
            {
                'title': 'quickly import i18n_utils.Translator from feffery-dash-utils',
                'prefix': 'utils:i18n',
                'description': 'Code snippet to import i18n_utils.Translator from feffery-dash-utils quickly',
                'body_path': r'raw_snippets\py\utils_i18n.py',
            },
        ],
    },
    {
        'name': 'client-side-snippets',
        'language': 'javascript',
        'items': [
            {
                'title': 'quickly initialize the structure of the client side callback function',
                'prefix': 'callback:init',
                'description': 'Quickly initialize the structure of the client side callback function',
                'body_path': r'raw_snippets\js\callback_init.js',
            },
            {
                'title': 'dash.no_update in client side',
                'prefix': 'callback:no_update',
                'description': 'dash.no_update in client side',
                'body_path': r'raw_snippets\js\callback_no_update.js',
            },
            {
                'title': 'PreventUpdate in client side',
                'prefix': 'callback:PreventUpdate',
                'description': 'PreventUpdate in client side',
                'body_path': r'raw_snippets\js\callback_prevent_update.js',
            },
            {
                'title': 'dash.ctx in client side',
                'prefix': 'callback:ctx',
                'description': 'dash.ctx in client side',
                'body_path': r'raw_snippets\js\callback_ctx.js',
            },
            {
                'title': 'set_props() in client side',
                'prefix': 'callback:set_props',
                'description': 'set_props() in client side',
                'body_path': r'raw_snippets\js\callback_set_props.js',
            },
            {
                'title': 'dash.ctx.triggered in client side',
                'prefix': 'callback:triggered',
                'description': 'dash.ctx.triggered in client side',
                'body_path': r'raw_snippets\js\callback_triggered.js',
            },
            {
                'title': 'dash.ctx.triggered_id in client side',
                'prefix': 'callback:triggered_id',
                'description': 'dash.ctx.triggered_id in client side',
                'body_path': r'raw_snippets\js\callback_triggered_id.js',
            },
            {
                'title': 'dash.ctx.inputs_list in client side',
                'prefix': 'callback:inputs_list',
                'description': 'dash.ctx.inputs_list in client side',
                'body_path': r'raw_snippets\js\callback_inputs_list.js',
            },
            {
                'title': 'dash.ctx.inputs in client side',
                'prefix': 'callback:inputs',
                'description': 'dash.ctx.inputs in client side',
                'body_path': r'raw_snippets\js\callback_inputs.js',
            },
            {
                'title': 'dash.ctx.states_list in client side',
                'prefix': 'callback:states_list',
                'description': 'dash.ctx.states_list in client side',
                'body_path': r'raw_snippets\js\callback_states_list.js',
            },
            {
                'title': 'dash.ctx.states in client side',
                'prefix': 'callback:states',
                'description': 'dash.ctx.states in client side',
                'body_path': r'raw_snippets\js\callback_states.js',
            },
            {
                'title': 'dash.ctx.outputs_list in client side',
                'prefix': 'callback:outputs_list',
                'description': 'dash.ctx.outputs_list in client side',
                'body_path': r'raw_snippets\js\callback_outputs_list.js',
            },
        ],
    },
    {
        'name': 'css-snippets',
        'language': 'css',
        'items': [
            {
                'title': 'customize the scrollbar',
                'prefix': 'css>scrollbar',
                'description': 'Code snippet to customize the scrollbar',
                'body_path': r'raw_snippets\css\scrollbar.css',
            },
            {
                'title': 'customize the initial loading animation',
                'prefix': 'css>init-loading',
                'description': 'Code snippet to customize the initial loading animation',
                'body_path': r'raw_snippets\css\init-loading.css',
            },
        ],
    },
    {
        'name': 'json-snippets',
        'language': 'json',
        'items': [
            {
                'title': 'locales',
                'prefix': 'locales',
                'description': 'Code snippet to generate template translations locales JSON file for feffery-dash-utils.i18n_utils.Translator',
                'body_path': r'raw_snippets\json\locales.json',
            }
        ],
    },
    {
        'name': 'server-side-template-snippets',
        'language': 'python',
        'items': [
            {
                'title': 'basic tool',
                'prefix': 'template:basic_tool',
                'description': 'Quickly generate code template for basic tool type app',
                'body_path': r'raw_snippets\py\templates\basic_tool.py',
            }
        ],
    },
]


if __name__ == '__main__':
    for category in raw_snippets:
        with open(
            './snippets/{}.code-snippets'.format(
                category['name']
            ),
            'w',
            encoding='utf-8',
        ) as f:
            json.dump(
                {
                    item['title']: {
                        'prefix': item['prefix'],
                        'body': [
                            open(
                                item['body_path'],
                                encoding='utf-8',
                            ).read()
                        ],
                        'description': item['description'],
                    }
                    for item in category['items']
                },
                f,
                indent=2,
                ensure_ascii=False,
            )
