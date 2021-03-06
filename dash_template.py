
import datetime
import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html


start_year = "2016"
start_month = "1"
start_day = "1
stock = "AMZN"  #The stock we want to see the information of


start = datetime.datetime(start_year, start_month, start_day)
end = datetime.datetime.now()


df = web.DataReader( stock, 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

#print(df.head())

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Stock information graph'),

    html.Div(children='''
        Making a stock graph!.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
            ],
            'layout': {
                'title': stock
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
