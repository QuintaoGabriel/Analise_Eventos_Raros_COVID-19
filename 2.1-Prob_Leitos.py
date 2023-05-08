import math
import matplotlib.pyplot as plt
import numpy as np

#MATRIZDE TRANSIÇÃO 7 Dias
'''Q = np.array([[0.95484323, 0.04515677],
              [0.05480517, 0.94519483]])'''

#MATRIZDE TRANSIÇÃO 14 Dias
Q = np.array([[0.87992431, 0.12007569],
              [0.10459513, 0.89540487]])

#TAMANHO DA MATRIZ
T = 100
I = np.zeros((T-1,1))

#Eixo horizontal
hor = np.zeros((T-1,1))

lista = []
v1 = 1
v2 = T
while v1 < T:
    hor[v1-1,0] = v1/T
    v2 = v2-1
    a = -(v2/T) * (1-Q[1,1]) * Q[0,0]
    b = (v1/T-v2/T)*(1-Q[1,1])*(1-Q[0,0])
    c = v1/T*(1-Q[0,0])*Q[1,1]
    delta = b*b - 4*a*c
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    if x1 <= 0 and x2 <= 0:
        lista.append(v1)
    else:
        if x1 > x2 :
            maior = x1
        else:
            maior = x2
        I[v1-1,0] = -(v1/T)*np.log(Q[0,0]+(1-Q[0,0])/maior)-(v2/T)*np.log((1-Q[1,1])*maior+Q[1,1])
    v1 = v1 + 1
 
print(I)

plt.plot(hor[:,0],I[:,0])
plt.axis([0, 1, 0, 0.05])
plt.title('IMAGEM 1')
plt.xlabel('x')
plt.ylabel('I(x)')
#plt.legend(['Sem Interação','Com Int g=0.1','Com Int/Sel g=0.1 s=5','Com Int/Sel g=0.1 s=10'],loc=0)
plt.savefig('RateFunctionLeitos14dias.png',format='png')
plt.show()

# station distribution
PIst = (1-Q[1,1])/(2-Q[0,0]-Q[1,1])

if PIst == PIst*Q[0,0]+(1-PIst)*(1-Q[1,1]):
    print('IGUAL')

print(PIst)

#df = pd.DataFrame(I)
#df.to_csv('Leitos14.csv')

lista_a = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
lista_inf = [max(I),max(I),max(I),max(I),max(I),max(I),max(I),max(I),max(I)]
cont = 0

for i in lista_a:
    x = (i + 0.01)
    while x <= max(hor):
        if lista_inf[cont] > I[int(x*100),0]:
            lista_inf[cont] = I[int(x*100),0]
        x = x + 0.01
    cont = cont + 1

print(f'INF1{lista_inf}\n')

lista_inf2 = [max(I),max(I),max(I),max(I),max(I),max(I),max(I),max(I),max(I)]
cont = 0

for i in lista_a:
    x = (i - 0.01)
    while x >= min(hor):
        if lista_inf2[cont] > I[int(x*100),0]:
            lista_inf2[cont] = I[int(x*100),0]
        x = x - 0.01
    cont = cont + 1

print(f'INF2{lista_inf2}\n')


resultado2 = 1
lista_final = []
for a in lista_inf:
    lista_final.append(np.exp(a * (-43)))

print(f'Prob1: {lista_final}\n')

resultado1 = 0
resultado2 = 1
lista_final2 = []

resultado2 = 1
lista_final2 = []
for a in lista_inf2:
    lista_final2.append(np.exp(a * (-86)))

print(f'Prob2: {lista_final2}')
