# matriz variavel rapida - uri 2520 - by mcavalca
n, m = [int(x) for x in input('linhas - colunas').split()]
matriz = []
for i in range(n):
    matriz.append(input().split())
print(matriz)
for l in range(0, n):
    for c in range(0, m):
        int(matriz[l][c])
for l in range(0, n):
    for c in range(0, m):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
