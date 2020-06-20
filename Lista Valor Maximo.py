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
