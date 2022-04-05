
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import numpy as np
import pandas as pd
import gunicorn #whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does
from whitenoise import WhiteNoise #for serving static files on WSGI web framework (Heroku) into static folder of root

# Instantiate dash app, and underlying flask app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE] ) #

# Define the underlying flask app as a variable called server. (Used by gunicorn webserver in Heroku production deployment)
server = app.server  

# Wrap the flask app with Whitenoise allowing serving static files from static folder (which is root to heroku)
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 

# Define Dash layout
def create_dash_layout(app):

    # Set browser tab title
    app.title = "Browser Tab Title" #browser tab
    
    # Header
    header = html.Div("Hi I am a header")
    
    # Body (i.e. the map centrepiece, with loaders to overlay ontop)
    body = html.Div("This is the body")

    # Footer
    footer = html.Div("This is the footer area")
    
    # Assemble dash layout 
    app.layout = html.Div([header, body, footer])

    return app


# Construct the dash layout
create_dash_layout(app)

# Run flask app
if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8050)























