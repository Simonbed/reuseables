import datetime
import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html


start_year = "2016"
start_month = "1"
start_day = "1

app.layout = html.Div(children=[
    html.Div(children='''
        Enter the symbol of the stock you want to show :
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def update_value(input_data):
  start = datetime.datetime(start_year, start_month, start_day)
  end = datetime.datetime.now()
  df = web.DataReader( stock, 'morningstar', start, end)
  df.reset_index(inplace=True)
  df.set_index("Date", inplace=True)
  df = df.drop("Symbol", axis=1)

  return dcc.Graph(
    id='example-graph',
    figure={
      'data': [
          {'x': df.index, 'y': df.Volume, 'type': 'bar', 'name': stock},
       ],
          'layout': {
              'title': stock
           }
       }
   )
])

if __name__ == '__main__':
    app.run_server(debug=True)
