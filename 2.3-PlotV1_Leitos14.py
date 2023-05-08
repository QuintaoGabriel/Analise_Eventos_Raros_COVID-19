import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abrindo a tabela
df = pd.read_csv('Leitos14.csv')

# Passando para um arranjo
z = np.array([df])

# Passando cada linha para dicionario
lista = []
dicionario = {}
cont = 0

while cont <= 9:
    dicionario[cont] = z[0][cont]
    cont = cont + 1


z1=dicionario[1][2:21]
z2=dicionario[2][2:21]
z3=dicionario[2][2:21]
z4=dicionario[3][2:21]
z5=dicionario[4][2:21]
z6=dicionario[5][2:21]
z7=dicionario[6][2:21]
z8=dicionario[7][2:21]
z9=dicionario[8][2:21]
z10=dicionario[9][2:21]


list = [1,2,3,4,5,6,7,8,9]

# Plotando
plt.plot(list,z1)

plt.plot(list,z3)

plt.plot(list,z5)

plt.plot(list,z7)

plt.plot(list,z9)

plt.title('Rate function')
plt.xlabel('v1')
plt.legend(['x=1','x=3','x=5','x=7','x=9'])

plt.show()