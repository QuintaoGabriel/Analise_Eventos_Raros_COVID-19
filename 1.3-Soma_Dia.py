import pandas as pd

relacao_df = pd.read_csv('RELACAO.csv')
datas_df = pd.read_csv('DATA.csv')

lista_datas_rec = []
lista_soma_datas_rec = []

# SOMANDO OS VALORES DE RECUPERADOS DE ACORDO COM A DATA
for datas in datas_df['DATA']:
    for x in relacao_df['NUM_INTERNADOS'].loc[relacao_df['DATA'] == datas]: 
        lista_datas_rec.append(x) # A LISTA RECEBE OS VALORES DE MESMA DATA
    lista_soma_datas_rec.append(sum(lista_datas_rec)) # A SEGUNDA LISTA RECEBE A SOMA DOS VALORES 
    lista_datas_rec.clear() # A PRIMEIRA LISTA É LIMPADA, PARA QUE RECEBA NOVAMENTE OS VALORES DA PRÓXIMA DATA

lista_datas_int = []
lista_soma_datas_int= []

# FAZENDO O MESMO PARA INTERNADOS
for datas in datas_df['DATA']:
    for x in relacao_df['NUM_INTERNADOS'].loc[relacao_df['DATA'] == datas]: 
        lista_datas_int.append(x)
    lista_soma_datas_int.append(sum(lista_datas_rec)) 
    lista_datas_int.clear() 

a = 0
b = 1
for i in lista_soma_datas_rec:
    datas_df.loc[a,'RECUPERADOS/DIA'] = lista_soma_datas_rec[b] - i
    a = a + 1
    if b <= 610:
        b = b + 1

a = 0
b = 1
for i in lista_soma_datas_rec:
    datas_df.loc[a,'INTERNADOS/DIA'] = lista_soma_datas_rec[b] - i
    a = a + 1
    if b <= 610:
        b = b + 1

datas_df.to_csv('RELACAO_DIA.csv',index=False)