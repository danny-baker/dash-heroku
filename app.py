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

# read data
df_country = pd.read_csv("https://raw.githubusercontent.com/smbillah/ist526/main/gapminder.csv")

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


# update graph
def update_figure(selected_year, asd):

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


# Run dash app
if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8050)
 
