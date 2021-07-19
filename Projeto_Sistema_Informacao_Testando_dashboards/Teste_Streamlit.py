#STREAMLIT TESTE

import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image

#streamlit run C:\Users\atsilva\Desktop\app.py


########################################################################

# Processamento Dados

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

#########################################################################

#juntando colunas
ppa_ind = pd.concat([ct,cult,des,desr,infr,sus,hidr,ges])

ppa_ind=ppa_ind.fillna({'Sugestão (manter/alterar/substituir)': 'Sem Sugestão'})

###########################################################################################

#ajustes na situação da reuniao setorial
#nome das colunas

ppa_ind['Situação da Reunião Setorial']=ppa_ind.loc[:,'Síntese Reunião Setorial'].isnull()

#situação das reuniões setoriais
ppa_ind=ppa_ind.replace({'Situação da Reunião Setorial': {True:'Reunião Não Registrada', False:'Houve Reunião'}})

################

#Filtrando falta de reuniao pegar os indices
sem_reuniao_ppa=ppa_ind[ppa_ind['Situação da Reunião Setorial']=='Reunião Não Registrada']

###############################################################################


# Parte Inicial

st.markdown("# Aplicativo Para Apresentação dos Programas do PPA 2020-2023")

st.markdown("Explore as informações referentes aos programas incluídos no PPA")

#Image.open(r'C:\Users\atsilva\Desktop\logo_seplan.png').convert('RGB').save('new.jpeg')

img=Image.open(r'C:\Users\atsilva\Desktop\Seplan-BA.jpg')

st.image(img,width=674)

st.markdown("**PPA** São Informações do Plano PluriAnual do Estado da Bahia, referente ao planejamento do estado da Bahia.")

st.markdown("Informações dos Programas do PPA")

#Parte interativa

if st.button("Conheça os Programas da Seplan BA"):
    img=Image.open(r'C:\Users\atsilva\Desktop\Programas_PPA.jpg')
    st.image(img,width=700, caption="Programas do PPA 2020-2023")
    #images=Image.open(r'C:\Users\atsilva\Desktop\new.jpeg')
  #  st.image(images,width=600)
    #Ballons
    #st.balloons()
    
st.markdown(
    "Os dados são provenientes da [Seplan-BA](http://www.seplan.ba.gov.br/arquivos/File/ppa/PPA2020_2023/05PPA_2020-2023_Publicado-TABELAS_RECURSOS_E_INDICADORES.pdf)")


























