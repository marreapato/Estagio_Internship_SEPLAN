import pandas as pd

ba=pd.read_excel("C:/Users/Usuário/Desktop/quantities/Indicadores_para_pente_fino_review.xlsx",sheet_name=None)

ba['query (2)'].columns.values

ba['query'].columns.values

#revisando:
#indicadores:
    
#ciencia e tecnologia 

ba['301']#ciencia e tecnologia

ct=ba['301']#ciencia e tecnologia
ct.columns.values

#Valores
ct.loc[:,'Apuração 2020']
ct.loc[:,'Valor de referência']

#Colunas de calculo

list(ct.loc[[0,4,5,9],'Memória de cálculo'])#5 apenas fala do valor de referencia
list(ct.loc[[0,4,5,9],'Informações complementares'])#5 apenas fala do valor de referencia
list(ct.loc[[0,4,5,9],'Informação para relatório legal'])#5 apenas fala do valor de referencia

#cultura 

ba['302']#cultura

cult=ba['302']#cultura
cult.columns.values

#Valores
cult.loc[:,'Apuração 2020']
cult.loc[:,'Valor de referência']

#Colunas de calculo

list(cult.loc[[7,8,9],'Memória de cálculo'])#
list(cult.loc[[7,8,9],'Informações complementares'])#apenas o 8
list(cult.loc[[7,8,9],'Informação para relatório legal'])

cult.loc[8,'Apuração 2020']=103.6


#desenvolvimento produtivo

ba['303']#desenvolvimento produtivo

des=ba['303']#desenvolvimento produtivo
des.columns.values

#Valores
des.loc[:,'Apuração 2020']
des.loc[:,'Valor de referência']

#Colunas de calculo

list(des.loc[[3,5,6,7],'Memória de cálculo'])#
list(des.loc[[3,5,6,7],'Informações complementares'])#apenas o 8
list(des.loc[[3,5,6,7],'Informação para relatório legal'])


##########################################33
#Salvando excel corrigido
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')
df3.to_excel(writer, sheet_name='Sheet3')

# Close the Pandas Excel writer and output the Excel file.
writer.save()


