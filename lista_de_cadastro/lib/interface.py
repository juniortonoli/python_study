def leiaint(msg):
    n = input(msg)
    while not n.isnumeric():
        print('Digite um numero valido!')
        n = input(msg)
    return int(n)


def linha(tam=42):
    return '_' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc
