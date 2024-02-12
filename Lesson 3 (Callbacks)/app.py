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

df = pd.read_csv("sample_data.csv")


def bar(x,y,title=''):
    fig = go.Figure()
    pie = go.Bar(x=x,y=y)

    fig.add_trace(pie) 
    fig.update_layout(title=title)
    return fig


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
                # "background": "cyan",
                "border-radius": "45px",
                "box-shadow": "10px 10px 20px rgba(0, 0, 0, 0.3)"
            }



### Designing Layout


header_row = dbc.Row( 

    [ 
        dbc.Col( 
            [ 
                html.H2("Callback Demo",style ={'textAlign':'center','color':'white'})
            ],md=11,style ={'background':'darkblue'}
        )
    ],justify ='center'
)



row_2 = dbc.Row( 
    [ 
        dbc.Col( 
            [ 
                html.H6("Select Merchant Size"),
                dcc.Dropdown(options=df.merchant_size.unique(),id='size',value='Small'),
                html.Br(),
                html.H6("Select Merchant Category"),
                dcc.Dropdown(options=df.category.unique(),id='cat',value='Eating and Drinking'),
                
            ],md=3,style=st
        ),

        dbc.Col( 
            [ 
                html.H5("Total Transaction Volume (BDT)"),
                html.Br(),
                html.Div(id='amount'),
            ],md=3,style=st
        ),
        dbc.Col( 
            [ 
                html.H5("Total Transaction Count"),
                html.Br(),
                html.Div(id='count'),
            ],md=3,style=st
        ),

    ],justify ='center'
)





graph_row = dbc.Row( 
    [ 
        dbc.Col( 
            [ 
                dcc.Graph(id='amount_bar')
            ],md=5,style=st
        ),
        dbc.Col( 
            [ 
                dcc.Graph(id='count_bar')
            ],md=5,style=st
        ),
    ],justify ='center'
)


app.layout = dbc.Container(

        [ 
            header_row,
            row_2,
            graph_row
        ]
     
     ,fluid=True)



@app.callback( 
    Output('amount_bar','figure'),
    Output('count_bar','figure'),

    Input('size','value'),
    Input('cat','value'),

)

def out(size,cat):
    graph_data = df[(df['merchant_size']==size) & (df['category']==cat)]

    g1 = bar(graph_data['division'],graph_data['amount'],'Amount')
    g2 = bar(graph_data['division'],graph_data['count'],'Count')


    return g1,g2




@app.callback( 
    Output('amount','children'),
    Output('count','children'),

    Input('size','value'),
    Input('cat','value'),

)

def out(size,cat):
    graph_data = df[(df['merchant_size']==size) & (df['category']==cat)]

    amt = graph_data['amount'].sum()
    cnt = graph_data['count'].sum()

    out_1 = html.H2(f"{amt}")
    out_2 = html.H2(f"{cnt}")

    return out_1,out_2




if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8999)
