import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import numpy as np
import pandas as pd
import matplotlib as mpl
import gunicorn                     #whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does
from whitenoise import WhiteNoise   #for serving static files on Heroku

# my header
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

## Instantiate dash app
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY]) 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define the underlying flask app (Used by gunicorn webserver in Heroku production deployment)
server = app.server 

# Enable Whitenoise for serving static files from Heroku (the /static folder is seen as root by Heroku) 
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),#'<h1> this is a header </h1>'
    #
    # html.Div(children='''
    #     Dash: A web application framework for Python.
    # '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Run dash app
if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8050)
 
