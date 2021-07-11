import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import plotly.graph_objects as go

#lendo excel sem queries
ba = pd.ExcelFile('C:/Users/Usuário/Desktop/quantities/Indicadores para pente fino_29-06-2021.xlsx')

#xlsx = pd.read_excel('C:/Users/Usuário/Desktop/quantities/Indicadores para pente fino_29-06-2021.xlsx',sheet_name=None)
#Segundo Query olhar depois

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

writer = pd.ExcelWriter('Indicadores_Para_Pente_Fino_semreuniao.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
table.to_excel(writer, sheet_name='table')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
