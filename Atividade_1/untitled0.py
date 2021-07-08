import pandas as pd

ba=pd.read_excel("C:/Users/Usuário/Desktop/quantities/Indicadores_para_pente_fino_review.xlsx",sheet_name=None)

ba['query (2)'].columns.values

ba['query'].columns.values

#ciencia e tecnologia 

ba['301']#ciencia e tecnologia

ct=ba['301']#ciencia e tecnologia

#drop NA
#https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan
