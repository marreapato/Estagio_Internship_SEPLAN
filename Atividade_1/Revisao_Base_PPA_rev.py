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


#desenvolvimento Rural

ba['304']#desenvolvimento rural

desr=ba['304']#desenvolvimento rural
desr.columns.values

#Valores
desr.loc[:,'Apuração 2020']
desr.loc[:,'Valor de referência']
#Colunas de calculo

list(desr.loc[[7,11,12,13,14],'Memória de cálculo'])#
list(desr.loc[[7,11,12,13,14],'Informações complementares'])#apenas o 8
list(desr.loc[[7,11,12,13,14],'Informação para relatório legal'])

desr.loc[[7,11,12,13,14],'Apuração 2020']

desr.loc[[11],'Apuração 2020']=(1299.12/1490)*100#possivelmente
desr.loc[[14],'Apuração 2020']=(29/417)*100#possivelmente

#infraestrutura

ba['309']#desenvolvimento rural

infr=ba['309']##infraestrutura
infr.columns.values

#Valores
infr.loc[:,'Apuração 2020']
infr.loc[:,'Valor de referência']

#Colunas de calculo
#2020
list(infr.loc[[7],'Memória de cálculo'])#valor de 2020

#ref
list(infr.loc[[1,7],'Memória de cálculo'])#valor de 2020
list(infr.loc[[1,7],'Informações complementares'])#apenas o 8
list(infr.loc[[1,7],'Informação para relatório legal'])

infr.loc[[7],'Apuração 2020']=(43/128) *100#possivelmente

###################################################
#Meio ambiente e sustentab

ba['310']#sustentabilidade

sus=ba['310']
sus.columns.values

#Valores
sus.loc[:,'Apuração 2020']
sus.loc[:,'Valor de referência']

#Colunas de calculo
#2020
list(sus.loc[[1,7,8],'Memória de cálculo'])#valor de 2020
list(sus.loc[[1,7,8],'Informações complementares'])#apenas o 8
list(sus.loc[[1,7,8],'Informação para relatório legal'])

###################################################
#recursos hidricos

ba['312']#hidricos

hidr=ba['312']
hidr.columns.values

#Valores
hidr.loc[:,'Apuração 2020']
hidr.loc[:,'Valor de referência']

#Colunas de calculo
#2020
list(hidr.loc[[0,1,2,3,5,8,9,10],'Memória de cálculo'])#valor de 2020
list(hidr.loc[[0,1,2,3,5,8,9,10],'Informações complementares'])#apenas o 8
list(hidr.loc[[0,1,2,3,5,8,9,10],'Informação para relatório legal'])

list(hidr.loc[[10],'Memória de cálculo'])#valor de 2020
hidr.loc[[0,1,2,3,5,8,9,10],'Apuração 2020']
hidr.loc[[10],'Apuração 2020']=29.24

list(hidr.loc[[3],'Memória de cálculo'])#valor de 2020
hidr.loc[[3],'Apuração 2020']=((1164887*0.711408269636008*2.99482018837047)/(3471239))*100

list(hidr.loc[[8],'Ano de referência'])#valor de 2020
list(hidr.loc[[8],'Memória de cálculo'])#valor de 2020
hidr.loc[[8],'Apuração 2020']=71.50


list(hidr.loc[[9],'Ano de referência'])#valor de 2020
list(hidr.loc[[9],'Memória de cálculo'])#valor de 2020
hidr.loc[[9],'Apuração 2020']=7.6


###################################################
#Gestao governamental

ba['315']#gestao

ges=ba['315']
ges.columns.values

#Valores
ges.loc[:,'Apuração 2020']
ges.loc[:,'Valor de referência']

##########################################33
#Salvando excel corrigido
writer = pd.ExcelWriter('Indicadores_Para_Pente_Fino_Revisados.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
ct.to_excel(writer, sheet_name='301')
cult.to_excel(writer, sheet_name='302')
des.to_excel(writer, sheet_name='303')
desr.to_excel(writer, sheet_name='304')
infr.to_excel(writer, sheet_name='309')
sus.to_excel(writer, sheet_name='310')
hidr.to_excel(writer, sheet_name='312')
ges.to_excel(writer, sheet_name='315')

# Close the Pandas Excel writer and output the Excel file.
writer.save()


