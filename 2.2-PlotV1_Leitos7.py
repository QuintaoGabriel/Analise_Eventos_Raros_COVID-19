import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abrindo a tabela
df = pd.read_csv('Leitos7.csv')

# Passando para um arranjo
z = np.array([df])

# Passando cada linha para dicionario
lista = []
dicionario = {}
cont = 0

while cont <= 19:
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
z11=dicionario[10][2:21]
z12=dicionario[11][2:21]
z13=dicionario[12][2:21]
z14=dicionario[13][2:21]
z15=dicionario[14][2:21]
z16=dicionario[15][2:21]
z17=dicionario[16][2:21]
z18=dicionario[17][2:21]
z19=dicionario[18][2:21]
z20=dicionario[19][2:21]

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

# Plotando
plt.plot(list,z1)

plt.plot(list,z5)

plt.plot(list,z10)

plt.plot(list,z15)

plt.plot(list,z19)

plt.title('Rate function')
plt.xlabel('v1')
plt.legend(['x=1','x=5','x=10','x=15','x=19'])

plt.show()