import datetime
import os
import dash
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State

# import style
# import graphs as gs


def bar(x,y):
    fig = go.Figure()
    pie = go.Bar(x=x,y=y)

    fig.add_trace(pie) 
    return fig

bar_graph = bar(["a","b"],[1,2])

# Initiate App
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

st ={
                "border": "1px solid black",
                "margin": "25px",
                "padding": "40px",
                "background": "cyan",
                "border-radius": "45px",
                "box-shadow": "10px 10px 20px rgba(0, 0, 0, 0.3)"
            }

### Designing Layout

row1 = dbc.Row(
    dbc.Col([html.H1("Title of the Dashboard", 
                     style={ 
                         'textAlign':'center',
                         'color':'darkgreen'
                     }
                     )], md=10),
    align="center",
    justify="center",
)


row2 = dbc.Row(
    [
        dbc.Col(
            [
                html.H1("H1 Header"),
                html.H2("H2 Header"),
                html.H3("H3 Header"),
                html.H4("H4 Header"),
                html.H5("H5 Header"),
                html.H6("H6 Header"),
                html.P("This is a paragraph"),
            ],
            md=5,
            style=st
        ),
        dbc.Col(
            [dcc.Graph(figure=bar_graph)],md=5,
            style= st
        ),
    ],    align="left",
    justify="center",
)


row3 = dbc.Row(
    dbc.Col(
        [
            dcc.Input(placeholder='Numeric Input',type='number'),
            html.Br(),

            dcc.Input(placeholder='Text Input',type='text'),
            html.Br(),

            dcc.Dropdown(options=["A", "B", "C"],value='A'),
            html.Br(),

            dcc.Dropdown(options=["A", "B", "C"], multi=True,value=['A']),
            html.Br(),

            dcc.RadioItems(options=["A", "B", "C"],value='A'),
            html.Br(),

            dcc.Checklist(options=["A", "B", "C"],value=['A']),
            html.Br(),

            dcc.Slider(1, 100),
            html.Br(),

            dbc.Button('Click'),
        ],
        md=5,style=st
    )
)


app.layout = dbc.Container([row1, row2, row3],fluid=False)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8999)
