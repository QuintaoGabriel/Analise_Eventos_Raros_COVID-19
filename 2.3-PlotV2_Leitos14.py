import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abrindo a tabela
df = pd.read_csv('Leitos14.csv')

# Passando para um arranjo
z = np.array([df])
y = np.transpose(z)

z1=y[1][1:21]
z2=y[2][1:21]
z3=y[2][1:21]
z4=y[3][1:21]
z5=y[4][1:21]
z6=y[5][1:21]
z7=y[6][1:21]
z8=y[7][1:21]
z9=y[8][1:21]
z10=y[9][1:21]


list = [1,2,3,4,5,6,7,8,9]

# Plotando
plt.plot(list,z1)

plt.plot(list,z3)

plt.plot(list,z5)

plt.plot(list,z7)

plt.plot(list,z9)

plt.title('Rate function')
plt.xlabel('v2')
plt.legend(['x=1','x=3','x=5','x=7','x=9'])

plt.show()