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

# uri 1182 escolhendo coluna / linha
import random
soma = 0
media = 0
matriz = []
linha = []
colunaescolhida = int(input(f'Digite a coluna escolhida: '))
linhaescolhida = int(input(f'Digite a linha escolhida: '))
qcoluna = [0] * 12
operacao = str(input(f'Somar ou Media: ')).lower()
# prenchendo matriz
for c in range(0, 12):
    matriz.append(qcoluna[:])
# escolhendo o numero (caso invalido)
for l in range(0, 12):
    for c in range(0, 12):
        matriz[l][c] = random.randint(1, 12)
# impressão de matriz
for l in range(0, 12):
    for c in range(0, 12):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
# definindo e operando valores escolhidos
print('Valores Escolhidos:')
for l in range(12):
    for c in range(12):
        if c == colunaescolhida:
            print(f'[{matriz[l][c]:^5}]', end='')
            soma = soma + matriz[l][c]
# condição de operação
print()
if operacao == 'somar':
    print(soma)
if operacao == 'media':
    print(soma / 12)

# matriz variavel alternate  (sem zeros)
matriz = []
qlinha = int(input(f'Digite quantas linhas: '))
qcoluna = int(input(f'Digite quantas colunas: '))
linhamatrix = []
# escolhendo numero
for l in range(0, qlinha):
    linhamatrix = []
    for c in range(0, qcoluna):
        numero = int(input(f'Digite um valor para [{l}, {c}] '))
        linhamatrix.append(numero)
    matriz.append(linhamatrix)
# impressão de matriz
for l in range(0, qlinha):
    for c in range(0, qcoluna):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
