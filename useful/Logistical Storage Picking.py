"""Se primeiro item (posição doca),começar do decrescente
Se meio do rack começar do mais proximo (lembrar ultima posição)
Se depositado (doca - posicao 0) começar descrecente


1 - 1 - 50 - 100

2 - 100 - 50 - 1


Se separacao terminar no 100 - 50, proximo corredor decrescente
Se separacao terminar no 1 - 50, proximo corredor crescente


listas = [int(n) for n in input().split('')]
print(listas)
positions = []
address = []
for c in range(0, len(listas), 2):
    positions.append([listas[c], listas[c+1]])
print(positions)
if positions[0][1] != positions[1][1]:
    print('Foi pro outro corredor')
    if positions[1][1] > 50:
        print('Fazer o proximo corredor descrecente')
else:
    print('Esta no mesmo corredor')"""

#logical storage picking crescent
#works if odd corridors are crescent and pair are decrescent. Distance Calculation.

listas = [int(n) for n in input().split()]
print(listas)
print(sorted(listas))
