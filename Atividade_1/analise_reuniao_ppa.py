import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.ticker as ticker
import plotly.express as px
import plotly.io as pio
from plotly.offline import plot
import dash
import dash_core_components as dcc
import dash_html_components as html

#lendo excel sem queries
ba = pd.ExcelFile("C:/Users/atsilva/Downloads/Indicadores para pente fino_29-06-2021.xlsx")
#indicadores:
   
#ciencia e tecnologia
ct=pd.read_excel(ba,'301')#ciencia e tecnologia

#cultura
cult=pd.read_excel(ba,'302')#cultura

#desenvolvimento produtivo
des=pd.read_excel(ba,'303')#desenvolvimento produtivo

#desenvolvimento Rural
desr=pd.read_excel(ba,'304')#desenvolvimento rural

#infraestrutura
infr=pd.read_excel(ba,'309')##infraestrutura

###################################################
#Meio ambiente e sustentab
sus=pd.read_excel(ba,'310')
###################################################
#recursos hidricos
hidr=pd.read_excel(ba,'312')
###################################################
#Gestao governamental
ges=pd.read_excel(ba,'315')
##########################################33
#juntando colunas
ppa_ind = pd.concat([ct,cult,des,desr,infr,sus,hidr,ges])

#preenchendo colunas vazias
ppa_ind.columns.values

ppa_ind.loc[:,'Sugestão (manter/alterar/substituir)']

ppa_ind=ppa_ind.fillna({'Sugestão (manter/alterar/substituir)': 'Sem Sugestão'})

# count plot on single categorical variable
geral=sns.countplot(x ='Sugestão (manter/alterar/substituir)', data = ppa_ind)
geral.set(xlabel='Sugestão', ylabel='',title='Situação dos indicadores revisados do PPA 2020-2023')
 
# Show the plot
# Some random data
ncount = len(ppa_ind)

# Also switch the labels over
geral.yaxis.set_label_position('right')

for p in geral.patches:
    x=p.get_bbox().get_points()[:,0]
    y=p.get_bbox().get_points()[1,1]
    geral.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y),
            ha='center', va='bottom') # set the alignment of the text


for p in geral.patches:
    geral.annotate(f'\n{p.get_height()}', (p.get_x()+0.25, p.get_height()+1), ha='center', va='top', color='white', size=18)

#geral.set_size_inches( 16, 10)

plt.show(geral)
#################################

ppa_ind.columns.values

ppa_ind['Situação da Reunião Setorial']=ppa_ind.loc[:,'Síntese Reunião Setorial'].isnull()

ppa_ind.loc[:,'Situação da Reunião Setorial']

#situação das reuniões setoriais
ppa_ind=ppa_ind.replace({'Situação da Reunião Setorial': {True:'Reunião Não Registrada', False:'Houve Reunião'}})

#contando criando pie plot
ppa_ind['Situação da Reunião Setorial'].value_counts()

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_format

reuger=ppa_ind['Situação da Reunião Setorial'].value_counts().plot(kind='pie', autopct = autopct_format(ppa_ind['Situação da Reunião Setorial'].value_counts()),shadow=True)
reuger.set(xlabel='', ylabel='',title='Situação da Reunião Setorial para discussão dos índices.')
plt.show(reuger)
################

#Filtrando falta de reuniao pegar os indices
sem_reuniao_ppa=ppa_ind[ppa_ind['Situação da Reunião Setorial']=='Reunião Não Registrada']


# count plot on single categorical variable
geral=sns.countplot(x ='Sugestão (manter/alterar/substituir)', data = sem_reuniao_ppa)
geral.set(xlabel='Sugestão', ylabel='',title='Situação dos Indicadores Sem Reunião Setorial Registrada')
 
# Show the plot
# Some random data
ncount = len(sem_reuniao_ppa)

# Also switch the labels over
geral.yaxis.set_label_position('right')

for p in geral.patches:
    x=p.get_bbox().get_points()[:,0]
    y=p.get_bbox().get_points()[1,1]
    geral.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y),
            ha='center', va='bottom') # set the alignment of the text


for p in geral.patches:
    geral.annotate(f'\n{p.get_height()}', (p.get_x()+0.25, p.get_height()+0.4), ha='center', va='top', color='white', size=18)

#geral.set_size_inches( 16, 10)
geral.fig.set_size_inches(15,15)
sns.despine(geral,left=True)

plt.show(geral)
#################################
sem_reuniao_ppa.columns
# count plot on single categorical variable
geral=sns.countplot(x ='Programa', data = sem_reuniao_ppa)
geral.set(xlabel='Programa', ylabel='',title='Programa dos Indicadores Com Reunião Não Registrada')

geral.set_xticklabels(geral.get_xticklabels(),rotation=40, ha="right")
#plt.tight_layout()
#plt.show()

# Show the plot
# Some random data
ncount = len(sem_reuniao_ppa)

# Also switch the labels over
geral.yaxis.set_label_position('right')

for p in geral.patches:
    x=p.get_bbox().get_points()[:,0]
    y=p.get_bbox().get_points()[1,1]
    geral.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y),
            ha='center', va='bottom') # set the alignment of the text


for p in geral.patches:
    geral.annotate(f'\n{p.get_height()}', (p.get_x()+0.25, p.get_height()+0.3), ha='center', va='top', color='white', size=10)

#geral.set_size_inches( 16, 10)
geral.fig.set_size_inches(15,15)
sns.despine(geral,left=True)

plt.show(geral)

#tabela para grafico no tableau

table=sem_reuniao_ppa.loc[:,['Programa','Descrição do Indicador','Sugestão (manter/alterar/substituir)']]

#pio.renderers.default='browser'
#plotly treemap

#para um futuro dash app
fig = px.treemap(table, path=['Programa','Sugestão (manter/alterar/substituir)','Descrição do Indicador'],template="seaborn",title="Sugestão e Indicadores Sem Reunião Registrada",
    labels=dict(labels="Analisando", parent="Informação Complementar", count="Quantidade"))
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25),uniformtext_minsize=64)
#ig.show()
##################

plot(fig)


#Alternativamente com polaridade



#tabela para grafico no tableau

table=sem_reuniao_ppa.loc[:,['Programa','Descrição do Indicador','Sugestão (manter/alterar/substituir)','Polaridade']]

#pio.renderers.default='browser'
#plotly treemap

#para um futuro dash app
fig = px.treemap(table, path=['Programa','Sugestão (manter/alterar/substituir)','Descrição do Indicador','Polaridade'],template="seaborn",title="Sugestão e Indicadores Sem Reunião Registrada",
    labels=dict(labels="Analisando", parent="Informação Complementar", count="Quantidade"))
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25),uniformtext_minsize=64)
#ig.show()
##################

plot(fig)

#Aplicativo dash
#teste para futuramente fazer um app dash

# initiate dataframe
df = table

# -*- coding: utf-8 -*-

#
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
fig = px.treemap(df, path=['Programa','Sugestão (manter/alterar/substituir)','Descrição do Indicador'],template="seaborn",title="Sugestão e Indicadores Sem Reunião Registrada",
    labels=dict(labels="Analisando", parent="Informação Complementar", count="Quantidade"))
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25),uniformtext_minsize=64)
#ig.show()

app.layout = html.Div(children=[
    html.H1(children='Reuniões Seplan'),

    html.Div(children='''
        Uma Aplicação no Dash.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server()
