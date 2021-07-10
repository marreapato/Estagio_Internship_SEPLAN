import pandas as pd

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
