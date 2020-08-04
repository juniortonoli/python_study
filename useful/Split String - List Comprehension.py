# split string without space - list comprehension

string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
comp = [string[i:i + n] for i in range(0, len(string), n)]
print(comp)

'''
string = '012345678998765432100123456789'
stringlist = []
tamanho = len(string) // 10
c = 0
for s in range(0, tamanho):
    stringlist.append(string[c:c+10])
    c = c + 10
print(stringlist)'''