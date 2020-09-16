'''file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas')
print(file.read())
print('#############')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#############')

file.seek(0, 0)
print(file.readlines())

file.close()'''

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

import os
os.remove('abc.txt')



