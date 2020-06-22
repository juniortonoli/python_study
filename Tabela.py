#Escreva um programa que leia dois valores X e Y. A seguir, mostre uma
# sequência de 1 até Y, passando para a próxima linha a cada X números.
# uri 1145


cont = 1
valorate = int(input('valorate:'))
numeroporlinha = int(input('numeroporlinha:'))
for linha in range(1, (int((valorate / numeroporlinha))+1)):
    print()
    for colunavalor in range(0, numeroporlinha):
        print(f'{cont} ', end='')
        cont = cont + 1

# algo com append

lista = []
# entrada
lin = int(input('quant linhas: '))
col = int(input('quant colunas: '))
print()

for linha in range(0, lin):
    lista.append(list())
    for coluna in range(0, col):
        lista[linha].append(list())
        lista[linha][coluna] = int(input(f'valor [{linha}, {coluna}]: '))
# saída
print(40*'-')
for linha in range(0, lin):
    for coluna in range(0, col):
        for celula in range(1):
            print(f'[{lista[linha][coluna]:^7}]', end='')
    print()
print(40*'-')
print('Encerrado.')

# matriz variavel
matriz = []
linha = int(input(f'Digite quantas linhas: '))
coluna = int(input(f'Digite quantas colunas: '))
qcoluna = [0] * coluna
for c in range(0, linha):
    matriz.append(qcoluna[:])
# escolhendo numero
for l in range(0, linha):
    for c in range(0, coluna):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
# impressão de matriz
for l in range(0, linha):
    for c in range(0, coluna):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
