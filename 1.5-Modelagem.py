import numpy as np
import pandas as pd
from hmmlearn import hmm

from hmmlearn.hmm import MultinomialHMM

np.random.seed(42)

df = pd.read_csv('OBS_COVID.csv') #Nesse campo alterne entre 7 e 14 dias.


model = hmm.MultinomialHMM(n_components=2, startprob_prior =1.0,transmat_prior =1.0,
                           algorithm='viterbi',random_state=None,n_iter=10000,tol=0.01,
                           verbose=False,params='ste',init_params=' ')


model.startprob_ = np.array([1/2, 1/2]) 

model.transmat_ = np.array([[95/100, 5/100], 
                            [7/100, 93/100]])

model.emissionprob_ = np.array([[99/100, 1/100],
                                [4/100, 96/100]])


Obs_sim1, Est_sim1 = model.sample(len(df),random_state=None) # faz uma simulação pelo dados inseridos

P1 = np.array([[df['OBSERVATION'][i]] for i in range(int(len(df)/2))]).astype(int)
P2 = np.array([[df['OBSERVATION'][i]] for i in range(int(len(df)/2), len(df))]).astype(int)

X = np.concatenate([P1,P2])
lengths = [len(P1), len(P2)]

log_modelo_inicial = model.score(X) 

import pickle
with open("modelo_inicial.pkl", "wb") as file: pickle.dump(model, file)

#modelo otimizado                               
model_opt = model.fit(X, lengths) 

Obs_sim2, Est_sim2 = model_opt.sample(len(df),random_state=None)

#score after optimization
log_modelo_opt = model_opt.score(X)

#print(log_modelo_opt)

model_opt.decode(X, lengths, algorithm='viterbi')

with open("modelo_otimizado.pkl", "wb") as file: pickle.dump(model_opt, file)

np.random.seed(42)

print('\nMatrizes otimizadas\n\n')
print('MATRIZ TRANSIÇÃO')
print(f'{model_opt.transmat_}\n\n')
print('MATRIZ EMISSÃO')
print(f'{model_opt.emissionprob_}\n\n')
print(f'{model_opt.startprob_}')

# criando um novo modelo 'comparativo' 

remodel = hmm.MultinomialHMM(n_components=2, n_iter=10000) 
remodel.fit(X)

#score after optimization
log_remodelo = remodel.score(X)

print(f'SCORE INICIAL: {log_modelo_inicial}')
print(f'\nSCORE OTIMIZADO: {log_remodelo}')

with open("modelo_otimizado_2.pkl", "wb") as file: pickle.dump(remodel, file)

# 1. Fazer mais testes ---> Melhor otimização possível
# 2. Com a matrizes iniciais... aplicar simulações
# 3. Comparar por meio de boxplot com óbitos diários
# 4. Gerar boxplot sim1 e sim2 ----> Qual está mais próximo do real??

# (Futuro) Utilizando os estados Est_sim1 --> Utilizar algoritmo de viterbi...
a = model_opt.decode(X, lengths, algorithm='viterbi')

viterbi_list = pd.DataFrame(a[1])

viterbi_list.to_csv('viterbi_list.csv', index = None)


internados = np.array([[df['SEMANAL'][i]] for i in range(len(df) - 1)]) # 0, 

df_obs2 = pd.DataFrame(Obs_sim2, columns = ['OBSERVATION'])
df_obs2['internados'] = np.array([[df['SEMANAL'][i]] for i in range(len(df))]) # 0, 
df_obs2.to_csv('obs_sim2.csv', index = None)

df_obs1 = pd.DataFrame(Obs_sim1, columns = ['OBSERVATION'])
df_obs1['internados'] = np.array([[df['SEMANAL'][i]] for i in range(len(df))]) 
df_obs1.to_csv('obs_sim1.csv', index = None)

# POSSO DEFINIR O LEN() QUE QUISER --> SIMULAR X DIAS DEPOIS DE LEN(DF) 

X, Z = model.sample(5)
print(f'Sequência prevista (5 semanas): {Z}')