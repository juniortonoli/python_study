ntests = int(input('Number of Tests: '))
finallist = []
templist = []
n = []
for c in range(ntests):
    n = [int(x) for x in input('Numeros: ').split()]
    for number in n:
        if number % 2 == 0:
            n.remove(number)
    while len(n) >= 1:
        templist.append(max(n))
        n.remove(max(n))
        templist.append(min(n))
        n.remove(min(n))
        if len(n) == 0:
            finallist.append(templist[:])
            templist.clear()
print(finallist)
print(n)

###################

ntests = int(input('Number of Tests: '))
templist = []
n = []
nodd = []
for c in range(ntests):
    n.clear()
    n = [int(x) for x in input('Numeros: ').split()]
    print(n)
    for number in n:
        if number % 2 != 0:
            nodd.append(number)
    while True:
        try:
            templist.append(max(nodd))
            nodd.remove(max(nodd))
        except:
            break
        try:
            templist.append(min(nodd))
            nodd.remove(min(n))
        except:
            break
    if len(nodd) == 1:
        templist.append(int(nodd[0]))
    for num in templist:
        print(num, end=' ')
    templist.clear()
    print()
