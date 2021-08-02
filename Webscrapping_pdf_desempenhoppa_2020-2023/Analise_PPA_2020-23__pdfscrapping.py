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
