import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import tabula
import os
import matplotlib.ticker as ticker
#
#webscraping table from pdf in web page
#Indicador de Eficácia das Metas (EXM) dos Programas 

#Tabela da página 20 do livro: http://www.seplan.ba.gov.br/arquivos/File/avaliacao_do_PPA/2020/relatorio_adp_v_final_ano_1_30042021_1042.pdf
table = tabula.read_pdf('relatorio_adp_v_final_ano_1_30042021_1042.pdf', pages="20")

table=table[0]

table.iloc[6,0]='306 – Educação'


#Mudar Virgula por ponto
table.iloc[:,1]=table.iloc[:,1].str.replace(',','.')


table.iloc[:,1]=pd.to_numeric(table.iloc[:,1], errors='coerce')
table.describe()

#indicador de eficacia das metas em media em 56.79%
#1/4 dos indicadores em ate 48,07% de eficacia
#valor maximo de 80,30% de eficacia

############################################


#Barplo
ax=sns.countplot(table["Conceito"],palette="Set3")  
plt.ylabel('Quantidade')

# Make twin axis
ax2=ax.twinx()

# Switch so count axis is on right, frequency on left
ax2.yaxis.tick_left()
ax.yaxis.tick_right()

# Also switch the labels over
ax.yaxis.set_label_position('right')
ax2.yaxis.set_label_position('left')

ax2.set_ylabel('Frequência [%]')
ncount=16
for p in ax.patches:
    x=p.get_bbox().get_points()[:,0]
    y=p.get_bbox().get_points()[1,1]
    ax.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y), 
            ha='center', va='bottom') # set the alignment of the text

# Use a LinearLocator to ensure the correct number of ticks
ax.yaxis.set_major_locator(ticker.LinearLocator(11))

# Fix the frequency range to 0-100
ax2.set_ylim(0,100)
ax.set_ylim(0,ncount)

# And use a MultipleLocator to ensure a tick spacing of 10
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))

# Need to turn the grid on ax2 off, otherwise the gridlines end up on top of the bars
ax2.grid(None)

################################################################

#Indicador de Eficácia das Metas (EXM) dos Programas 

table2 = tabula.read_pdf('relatorio_adp_v_final_ano_1_30042021_1042.pdf', pages="21-22")


#removendo linhas
table2[0]=table2[0].drop(table2[0].index[[0]])
table2[0].columns=['Programa','ExOFP (%)','Grau de Execução', 'Classificação da Execução']

table2[0].iloc[8,0]='307 ‐ Igualdade Racial, Povos e Comunidades Tradicionais'
table2[0]=table2[0].drop(table2[0].index[[7]])

#removendo colunas

table2[1]=table2[1].drop(table2[1].columns[[2,4,5,7]],axis=1)
table2[1].columns=['Programa','ExOFP (%)','Grau de Execução', 'Classificação da Execução']

table2[1].loc[7] = ['308 ‐ Inclusão Socioprodutiva e Mundo do Trabalho','61,11','3','Bom']  # adding a row

#concatenando linhas

table2=pd.concat(table2, keys=['Programa','ExOFP (%)','Grau de Execução', 'Classificação da Execução'],ignore_index=True)


table2.iloc[6,0]='306 – Educação'

#Mudar Virgula por ponto
table2.iloc[:,1]=table2.iloc[:,1].str.replace(',','.')


table2.iloc[:,1]=pd.to_numeric(table2.iloc[:,1], errors='coerce')
table2.describe()
table2.columns
#media do do indicador de execução orcamentaria é de 42.72% ou seja, em média os programas tiveram uma execução financeira regular

##########################################################
###########################################
########################
###########
######
###
##
#
#Barplo
ax=sns.countplot(table2["Classificação da Execução"],palette="Set3")  
plt.ylabel('Quantidade')

# Make twin axis
ax2=ax.twinx()

# Switch so count axis is on right, frequency on left
ax2.yaxis.tick_left()
ax.yaxis.tick_right()

# Also switch the labels over
ax.yaxis.set_label_position('right')
ax2.yaxis.set_label_position('left')

ax2.set_ylabel('Frequência [%]')
ncount=16
for p in ax.patches:
    x=p.get_bbox().get_points()[:,0]
    y=p.get_bbox().get_points()[1,1]
    ax.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y), 
            ha='center', va='bottom') # set the alignment of the text

# Use a LinearLocator to ensure the correct number of ticks
ax.yaxis.set_major_locator(ticker.LinearLocator(11))

# Fix the frequency range to 0-100
ax2.set_ylim(0,100)
ax.set_ylim(0,ncount)

# And use a MultipleLocator to ensure a tick spacing of 10
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))

# Need to turn the grid on ax2 off, otherwise the gridlines end up on top of the bars
ax2.grid(None)

#merging 2 datasets

table_full=pd.merge(left=table, right=table2, left_on='Programa', right_on='Programa')



############################################
table_full.columns.values


#Classificação do indicador de eficacia das metas por classificacao execução orçamentaria

#Barplo
ax=sns.countplot(table_full["Conceito"],palette="Set3",hue=table_full['Classificação da Execução'])  
plt.ylabel('Quantidade')

# Make twin axis
ax2=ax.twinx()

# Switch so count axis is on right, frequency on left
ax2.yaxis.tick_left()
ax.yaxis.tick_right()

# Also switch the labels over
ax.yaxis.set_label_position('right')
ax2.yaxis.set_label_position('left')

ax2.set_ylabel('Frequência [%]')
ncount=16
for p in ax.patches:
    x=p.get_bbox().get_points()[:,0]
    y=p.get_bbox().get_points()[1,1]
    ax.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y), 
            ha='center', va='bottom') # set the alignment of the text

# Use a LinearLocator to ensure the correct number of ticks
ax.yaxis.set_major_locator(ticker.LinearLocator(11))

# Fix the frequency range to 0-100
ax2.set_ylim(0,100)
ax.set_ylim(0,ncount)

# And use a MultipleLocator to ensure a tick spacing of 10
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))

# Need to turn the grid on ax2 off, otherwise the gridlines end up on top of the bars
ax2.grid(None)
