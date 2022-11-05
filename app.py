import dash
from dash.dependencies import Input, Output, State

app = dash.Dash()

@app.callback(
    Output('', ''),
    Input('', ''),
)
def callback_func():

    return dash.no_update