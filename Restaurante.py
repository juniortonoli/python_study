#Append, soma de itens do cardapio.

data = [{'codigo': 0, 'nome': 'Cachorro Quente', 'preco': 4},
        {'codigo': 1, 'nome': 'X Salada', 'preco': 3},
        {'codigo': 2, 'nome': 'X Bacon', 'preco': 5}]
pedido = []
#0 quantidade 1 nome 2 precototal
item = []
opcao = 's'
total = 0
while opcao == 's':
    codigo = int(input('Codigo:'))
    quantidade = int(input('Quantidade:'))
    item.append(quantidade)
    item.append(data[codigo]["nome"])
    item.append(quantidade * data[codigo]["preco"])
    total = total + item[2]
    pedido.append(item[:])
    item.clear()
    opcao = str(input('Pedir mais itens? S ou N?')).lower()
for c in range(len(pedido)):
    print(f'{pedido[c][0]} {pedido[c][1]}, Total: R$: {pedido[c][2]}')
print(f'Total do pedido: {total}')
# if opcao == 's':

# print(f'Pedido de {quantidade} {data[codigo]["nome"]}: Valor Total: R$ {quantidade * data[codigo]["preco"]}')
