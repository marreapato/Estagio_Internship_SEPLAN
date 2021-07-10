import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


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

# Make twin axis
#ax2=geral.twinx()

# Switch so count axis is on right, frequency on left
#ax2.yaxis.tick_left()
#geral.yaxis.tick_right()

# Also switch the labels over
geral.yaxis.set_label_position('right')
#ax2.yaxis.set_label_position('left')

#ax2.set_ylabel('[%]')

for p in geral.patches:
    x=p.get_bbox().get_points()[:,0]
    y=p.get_bbox().get_points()[1,1]
    geral.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y), 
            ha='center', va='bottom') # set the alignment of the text

# Fix the frequency range to 0-100
#ax2.set_ylim(0,100)
#geral.set_ylim(0,ncount)

# And use a MultipleLocator to ensure a tick spacing of 10
#ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))

# Need to turn the grid on ax2 off, otherwise the gridlines end up on top of the bars
#ax2.grid(None)

for p in geral.patches:
    geral.annotate(f'\n{p.get_height()}', (p.get_x()+0.25, p.get_height()+1), ha='center', va='top', color='white', size=18)

#geral.set_size_inches( 16, 10)
geral.fig.set_size_inches(15,15)
sns.despine(geral,left=True)


plt.show(geral)
