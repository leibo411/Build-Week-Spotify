# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            ##### Find the song ID of a song you enjoy listening to and paste it into the prediction generator to disvover new music.

            In order to find the song ID, open spotify and search for the song you would like to use. Click on "..." next to the song and navigate to the share tab. Copy the song link and paste it into a notes page.

            The result should look something like,

            https://open.spotify.com/track/5ervA7lbl13K2ekOUFmgKe

            The numbers and letters following /track/ are the song ID. Input this into the prediction generator to discover new music.

            """
        ),
    ],
    md=6,
)

input_types = ['text']
column2 = dbc.Col(
    [

                html.Label('Song ID: '),
                dcc.Input(id='input-1-submit', type='text', placeholder='Enter ID'),
                html.Br(),html.Br(),
                html.Button('Submit', id='btn-submit'),
                html.Br(),
                html.Hr(),
                html.Label('Track ID'), html.Br(),html.Br(),
                html.Div(id='output-submit'),
                html.Br(), html.Hr()
                # html.Div(id='output-submit', style={'display': 'none'})
    ]
)


layout = dbc.Row([column1, column2])

html.Div(id='intermediate-value', style={'display': 'none'})


@app.callback(Output('output-submit', 'children'),
                [Input('btn-submit', 'n_clicks')],
                [State('input-1-submit', 'value')])
def update_output(clicked, input1):
    if clicked:
        track_id = input1
        pd.DataFrame([track_id]).to_csv('track_id.csv')
        return 'Track ID is => ' + track_id


# print(track_id)