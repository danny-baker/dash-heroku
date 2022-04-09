## mandatory import for heroku (do not change)
import gunicorn                     #needed for Heroku's linux webserver (i.e. dyno)
from whitenoise import WhiteNoise   #for serving static files on Heroku

# mandatory dash import (do not change)
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input


import plotly.express as px
import math
from dash import no_update

## ohter imports
import pandas as pd
import numpy as np
import json
import matplotlib as mpl

## your imoprt
# none (for now)

## this css creates columns and row layout
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


## Uncomment the following line for runnning in Google Colab
#app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

## Uncomment the following line for running locally in a webbrowser
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

## Define the underlying flask app (Used by gunicorn webserver in Heroku production deployment)
server = app.server 

## Enable Whitenoise for serving static files from Heroku (the /static folder is seen as root by Heroku)
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 

## read data
df_country = pd.read_csv("https://raw.githubusercontent.com/smbillah/ist526/main/gapminder.csv")

## creating layout
app.layout = html.Div([
    # first row: header
  html.H4('A Sample Dashboard'),

  # second row: <scratter-plot + slider> <empty> <debug> 
  html.Div([
            
    # scratter plot                      
    html.Div([
              
      # add scatter plot
      dcc.Graph(
        id='scatter-graph',
        figure=None # we'll create one inside update_figure function
      ),

      # add slider
      dcc.Slider(
        id='year-slider',
        min=df_country['year'].min(),
        max=df_country['year'].max(),
        value=df_country['year'].min(),
        marks={str(year): str(year) for year in df_country['year'].unique()},
        step=None
      )
    ], className = 'six columns'),   

    html.Div([
      html.H3('Debug'),
      #html.Br(),
      html.P(id='output_text_1', children='Total:'),
      html.P(id='output_text_2', children='Details:'),
      html.P(id='output_text_3', children='Conclusion:')
    ], className = 'six columns')
  ], className = 'row')    
])

# add callback for input. Note that we have two output: one for the figure, and another for debugging. We'll display input parameter in an html.P(id='output_text_1)
@app.callback(
  Output('scatter-graph', 'figure'),
  Output('output_text_1', 'children'), #for debugging purpose
  Input('year-slider', 'value')
)

# callback function: update function
def update_figure(selected_year):

  # put the input parameter in debug_params variable
  debug_params ='Input: {0}'.format(selected_year)

  # filter data frame based on selected_year. Note that the value of selected_year is coming from the slider
  filtered_df = df_country[df_country.year == selected_year]
  
  # note that this fig is the same as HW5.Q2(a) 
  fig_scatter = px.scatter(
    data_frame = filtered_df, 
    x="gdpPercap",         # gdp per capita
    y="lifeExp",           # life expectancy  
    size="pop",            # population
    color="continent",     # group/label
    hover_name="country",
    log_x=True, 
    size_max=55, 
    range_x=[100,100000], 
    range_y=[25,90],
    title= "GDP Per Captia vs Life Expectancy of Countries",     
  )  

  # fig_scatter.update_layout(transition_duration=500)

  # return two output separated by comma
  return fig_scatter, debug_params
# end update_


### run the code

## uncomment the following line to run in Google Colab
#app.run_server(mode='inline', port=8030)

## uncomment the following 2 lines to run locally in a Browser via command line/terminal
#if __name__ == '__main__':
#  app.run_server(debug=True, host='127.0.0.1', port=8000)


## uncomment the following 2 lines to run remotely on heroku server
if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8050)
 
