import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import tabula
import os

#

#webscraping table from pdf in web page
#Indicador de Eficácia das Metas (EXM) dos Programas 

#Tabela da página 20 do livro: http://www.seplan.ba.gov.br/arquivos/File/avaliacao_do_PPA/2020/relatorio_adp_v_final_ano_1_30042021_1042.pdf
table = tabula.read_pdf('relatorio_adp_v_final_ano_1_30042021_1042.pdf', pages="20")

table=table[0]

table.iloc[6,0]='306 – Educação'
