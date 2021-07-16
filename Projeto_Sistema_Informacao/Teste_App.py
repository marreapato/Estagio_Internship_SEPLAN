#Dash App de teste

import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc#adiciona interatividade ao dash
import plotly.express as px
from dash.dependencies import Input, Output


df=pd.read_csv("https://raw.githubusercontent.com/STATWORX/blog/master/DashApp/data/stockdata2.csv",index_col=0,parse_dates=True)

#transformando string datas em Date object

df.index = pd.to_datetime(df['Date'])

# Lista de dicionarios, com keys 'label' e 'value'.
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list




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
    html.P('''Selecione uma Opção de Teste.'''),
    
    
    #############################################################
    html.Div(className='div-for-dropdown',
          children=[
              dcc.Dropdown(id='stockselector',
                           options=get_options(df['stock'].unique()),
                           multi=True,
                           value=[df['stock'].sort_values()[0]],
                           style={'backgroundColor': '#1E1E1E'},
                           className='stockselector')
                    ],
          
          style={'color': '#1E1E1E'})#nova child com a funcao get options
    
    
    
    
]),  # Definindo elemento da coluna esquerda
                                  html.Div(className='eight columns div-for-charts bg-grey',children = [dcc.Graph(id='timeseries',
          config={'displayModeBar': False}),
             dcc.Graph(id='change', config={'displayModeBar': False})])  # Definindo elemento da direita
                                  ])
                                ])


# Run the app
if __name__ == '__main__':
    
    app.run_server(debug=False)
    
##############################################

