import pandas as pd

tabela_df = pd.read_csv('RELACAO.csv')

#CRIANDO UM ARQUIVO CSV APENAS COM A COLUNA DE DATAS
data_df = tabela_df[['DATA']]

#REMOVE AS DATAS DUPLICADAS
data_unique_df = data_df.drop_duplicates()

data_unique_df.to_csv('DATA.csv',index=False)