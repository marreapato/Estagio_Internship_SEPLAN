#STREAMLIT TESTE https://towardsdatascience.com/build-your-first-data-visualization-web-app-in-python-using-streamlit-37e4c83a85db

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


st.info("O plano PluriAnual é Realizado de 4 em 4 anos e contém informações referente ao desenvolvimento de todo o estado da Bahia.")
img=Image.open(r'C:\Users\atsilva\Desktop\nucleo_territorial_educacao_2018.jpg')
st.image(img,width=700,caption = "fonte: SEI - Superintendência de Estudos Econômicos e Sociais da Bahia (https://www.sei.ba.gov.br/index.php?option=com_content&view=category&id=1500&Itemid=101)")

##################################################################################################

#Painel lateral

st.sidebar.markdown("## Painel Lateral")
st.sidebar.markdown("Use esse painel para explorar o app e criar interações.")

#df = pd.read_csv(DATA_URL, nrows = nrows)
 #   lowercase = lambda x:str(x).lower()
  #  df.rename(lowercase, axis='columns',inplace=True)
   # return df

st.header("Explore a Base de dados do PPA revisado")

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Baixando Base de dados do PPA do Programa de Gestão Governamental...')
    # Load 10,000 rows of data into the dataframe.
ges
df = ppa_ind

# Notify the reader that the data was successfully loaded.

data_load_state.text('Baixando base de dados do PPA do Programa de Gestão Governamental...Completo!')

images=Image.open(r'C:\Users\atsilva\Desktop\new.jpeg')

st.image(images,width=200)


##################################################
#interação painel lateral check box

if st.checkbox("Mostrar Todos Os Dados de todos os Programas", False):
    st.subheader('Todos Os Dados')
    st.write(df)
st.title('Explorando...')
st.sidebar.subheader(' Exploração Breve')
st.markdown("Marque a caixinha no painel lateral para explorar os dados.")
if st.sidebar.checkbox('Informação Básica'):
    #if st.sidebar.checkbox('Breve exploração da base'):
        #st.subheader('Exploração Breve:')
       # st.write(df.head())
    if st.sidebar.checkbox("Mostrar Colunas"):
        st.subheader('Mostrar Lista de Colunas')
        all_columns = df.columns.to_list()
        st.write(all_columns)
   
    if st.sidebar.checkbox('Descrição Estatística'):
        st.subheader('Dados da Descrição Estatística')
        st.write(df.describe())
    if st.sidebar.checkbox('Valores Faltantes?'):
        st.subheader('Valores Faltantes')
        st.write(df.isnull().sum())



if st.sidebar.checkbox('Exploração Breve Da Base'):
        st.subheader('Breve Exploração dos Dados:')
        st.write(df.head())














