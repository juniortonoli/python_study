# lista valor maximo
'''import random
valor = list(range(1, 101))
random.shuffle(valor)
maxvalue = max(valor)
maxindex = valor.index(maxvalue)
print(valor)
print(maxvalue)
print(maxindex)'''

#range de lista

lista = 0
while True:
    x = int(input('valor:'))
    if x == 0:
        break
    else:
        lista = list(range(1, x+1))
        for c in lista:
            if c == x:
                print(f'{c}', end='')
            else:
                print(f'{c} ', end='')
        print()

#selecao em lista
vetor = []
for c in range(0, 11):
    x = int(input(f'valor X:'))
    vetor.append(x)
for k, v in enumerate(vetor):
    if v <=10:
        print(f'{k} = {v}')
# selecao em lista alternate
# A=[]
# for i in range(100):
#     x = float(input())
#     A.append(x)
#     if x <=10.0:
#         print('A[{}] = {}'.format(i,x))

# criando uma lista com base na outra, reverse [start:stop:step]
N=[]
for i in range(20):
    x=int(input())
    N.append(x)
a=N[::-1]
for j in range(20):
    print('N[{}] = {}'.format(j,a[j]))

# [min maximo lista e index]

n = int(input(f'valor n:'))
lista = []
for c in range(n):
    x = int(input(f'valor X{c}:'))
    lista.append(x)
print(f' {min(lista)}')
print(f' {lista.index(min(lista))}')