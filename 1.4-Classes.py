import numpy as np
import pandas as pd

df = pd.read_csv('RELACAO_DIA.csv')

# CONSIDERANDO A REFERENCIA DE 7 E 14 DIAS
data_ref = 7, 14
for j in (data_ref):
    df['cases_' + str(j)] = 0
    for i in range(len(df) - j):
        df['cases_' + str(j)][i] = df['INTERNADOS/DIA'][i + j] 

# SEPARANDO POR CLASSES 0,1,2(ABAIXO DA MEDIA, NA MEDIA, ACIMA DA MEDIA) 

for j in (data_ref):
    df['observation_' + str(j)] =  0
    for i in range(len(df)):
        if df['cases_' + str(j)][i] <= np.quantile(df['cases_' + str(j)], 0.25):
           df['observation_' + str(j)][i] = 0
        if  np.quantile(df['cases_' + str(j)], 0.25) < df['cases_' + str(j)][i] <= np.quantile(df['cases_' + str(j)], 0.75):
           df['observation_' + str(j)][i] = 1
        if np.quantile(df['cases_' + str(j)], 0.75) < df['cases_' + str(j)][i]:
           df['observation_' + str(j)][i] = 2

df.to_csv('OBS_COVID.csv')