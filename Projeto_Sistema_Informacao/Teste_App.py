#Dash App de teste

import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc#adiciona interatividade ao dash
import plotly.express as px

df=pd.read_csv("https://raw.githubusercontent.com/STATWORX/blog/master/DashApp/data/stockdata2.csv",index_col=0,parse_dates=True)

#transformando string datas em Date object

df.index = pd.to_datetime(df['Date'])

# app inicializando

###############################################

#Estrutura de teste

app = dash.Dash(__name__)

#layout do app

app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='four columns div-user-controls',children = [
    html.H2('Dash Teste de App'),
    html.P('''Teste de app com Plotly - Dash'''),
    html.P('''Selecione uma Opção de Teste.''')
]),  # Definindo elemento da coluna esquerda
                                  html.Div(className='eight columns div-for-charts bg-grey',children = [dcc.Graph(id='timeseries',
          config={'displayModeBar': False},
          animate=True,
          figure=px.line(df,
                         x='Date',
                         y='value',
                         color='stock',
                         template='seaborn').update_layout(
                                   {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )])  # Definindo elemento da direita
                                  ])
                                ])


# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
    
##############################################

