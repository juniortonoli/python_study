lista = [['p1', 13],
         ['p2', 6],
         ['p3', 50]
]


def func(item):
    return item[1]


#lista.sort(key=func)
lista.sort(key=lambda item: item[1])
print(lista)

