#Count how many types there are in a list, with counter.

from collections import Counter
dados = ['))', '))', ')', '(', '(']
contagem = (Counter(dados))
print(len(contagem))

#or use set() function with len() function

dados = ['))', '))', ')', '(', '(']
dados = set(dados)
print(len(dados))
