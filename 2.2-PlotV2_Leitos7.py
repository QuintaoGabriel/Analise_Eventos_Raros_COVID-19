import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abrindo a tabela
df = pd.read_csv('Leitos7.csv')

# Passando para um arranjo
z = np.array([df])
y = np.transpose(z)


z1=y[2][1:21]
z2=y[2][1:21]
z3=y[2][1:21]
z4=y[3][1:21]
z5=y[4][1:21]
z6=y[5][1:21]
z7=y[6][1:21]
z8=y[7][1:21]
z9=y[8][1:21]
z10=y[9][1:21]
z11=y[10][1:21]
z12=y[11][1:21]
z13=y[12][1:21]
z14=y[13][1:21]
z15=y[14][1:21]
z16=y[15][1:21]
z17=y[16][1:21]
z18=y[17][1:21]
z19=y[18][1:21]
z20=y[19][1:21]

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

# Plotando
plt.plot(list,z1)

plt.plot(list,z5)

plt.plot(list,z10)

plt.plot(list,z15)

plt.plot(list,z19)

plt.title('Rate function')
plt.xlabel('v2')
plt.legend(['x=1','x=5','x=10','x=15','x=19'])

plt.show()