import pandas as pd

#IMPORTAR OS ARQUIVO DE DADOS
internados_df = pd.read_excel('INTERNADOS.xlsx')    #INTERNADOS POR COVID
recuperados_df = pd.read_excel('RECUPERADOS.xlsx')  #INTERNADOS RECUPERADOS

#DEIXANDO TUDO NA MESMA TABELA
relacao_df = pd.merge(internados_df,recuperados_df)
relacao_df.to_csv('RELACAO.csv',index=False) #SALVANDO COMO CSV 