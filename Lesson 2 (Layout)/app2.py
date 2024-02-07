import dash
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State




# Initiate App
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],
    # suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

row1 = dbc.Row( 
    [ 
        dbc.Col( 
            [ 
                html.H1("TITLE",style={'textAlign':'center'})
            ],md=11
        )
    ],justify='center'
)


row2 = dbc.Row( 
    [ 
        dbc.Col( 
            [   html.H6("Dropdown 1"),
                dcc.Dropdown(options=['A',"B"])
                ],md=3
        ),
        dbc.Col( 
            [   html.H6("Dropdown 2"),
                dcc.Dropdown(options=['A',"B"])
                ],md=3
        ),
        dbc.Col( 
            [
                html.H6("Radio 1"),
                dcc.RadioItems(options=['A',"B"])
            ],md=3
        ),

    ],justify='center'
) 


row3 = dbc.Row( 
    [ 
        dbc.Col( 
            [ 
                dcc.Graph()
            ],md =5
        ),
        dbc.Col( 
            [ 
                dcc.Graph()
            ],md=5
        ),
    ],justify='center'
)




app.layout = dbc.Container( 
    [ 
        row1,row2,row3
    ]
)




if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8999)
