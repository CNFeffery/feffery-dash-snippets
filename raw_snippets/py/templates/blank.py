# 这是一个最基础的空白Dash应用模板，由feffery-dash-snippets自动生成

import dash
from dash import html
from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        
    ],
    style=style(padding=50)
)

if __name__ == '__main__':
    app.run(debug=True)