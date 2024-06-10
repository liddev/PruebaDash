import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
df = pd.DataFrame({
    "X": [1, 2, 3, 4, 5],
    "Y": [10, 15, 13, 17, 18]
})

app = dash.Dash(__name__)

app.layout = html.Div(style={'backgroundColor': 'black', 'color': 'white'}, children=[
    html.H1(children='Prueba'),

    html.Div(children='''
        Prueba de despliegue con Render.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=px.scatter(df, x="X", y="Y", title="Dispersión").update_layout(template='plotly_dark')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)