'''hora_inicial = int(input(f'Digite HI: '))
minuto_inicial = int(input(f'Digite MI: '))
hora_final = int(input(f'Digite HF: '))
minuto_final = int(input(f'Digite MF: '))
thoras = 0
tminutos = 0

if hora_final > hora_inicial:
    if hora_final - hora_inicial == 1:
        if minuto_final >= minuto_inicial:
            thoras = 0
            tminutos = minuto_final - minuto_inicial
            print(f' Tempo de jogo: {thoras} horas e {tminutos} minutos.')
        if minuto_final < minuto_inicial:#erro
            thoras = 0
            tminutos = (60 - minuto_inicial) + minuto_final
            print(f' Tempo de jogo: {thoras} horas e {tminutos} minutos.')
    elif minuto_final >= minuto_inicial: #testado
        thoras = hora_final - hora_inicial
        tminutos = minuto_final - minuto_inicial
        print(f' Tempo de jogo: {thoras} horas e {tminutos} minutos.')
    elif minuto_final < minuto_inicial: #testado
        thoras = (hora_final - hora_inicial) - 1
        tminutos = (60 - minuto_inicial) + minuto_final
        print(f' Tempo de jogo: {thoras} horas e {tminutos} minutos.')


if hora_final == hora_inicial:
    if minuto_final >= minuto_inicial: #testado
        thoras = 0
        tminutos = minuto_final - minuto_inicial
        print(f' Tempo de jogo: {thoras} horas e {tminutos} minutos.')
    if minuto_final == minuto_inicial: #testado
        print('Tempo de jogo: 24 horas')
    if minuto_final < minuto_inicial:
        thoras = 23
        tminutos = tminutos = (60 - minuto_inicial) + minuto_final
        print(f' Tempo de jogo: {thoras} horas e {tminutos} minutos.')



if hora_final < hora_inicial:
    if minuto_final >= minuto_inicial: #testado
        thoras = (24 - hora_inicial) + hora_final
        tminutos = minuto_final - minuto_inicial
        print(f' Tempo de jogo: {thoras} horas e {tminutos} minutos.')
    if minuto_final < minuto_inicial: #testado
        thoras = (24 - hora_inicial) + hora_final - 1
        tminutos = (60 - minuto_inicial) + minuto_final
        print(f' Tempo de jogo: {thoras} horas e {tminutos} minutos.')
print()

from datetime import datetime
from datetime import timedelta
hora_inicial = int(input(f'Digite HI: '))
minuto_inicial = int(input(f'Digite MI: '))
hora_final = int(input(f'Digite HF: '))
minuto_final = int(input(f'Digite MF: '))

ttime = timedelta(hours=hora_inicial,  minutes=minuto_inicial)
print(ttime)
horateste = timedelta(hours=hora_final,  minutes=minuto_final) - ttime
print(horateste.hour)'''

import datetime

#date manual, diminuindo
# d = datetime.date(2016, 7, 24)
# e = datetime.date(2015, 6, 20)
# a = d - e
# print(a)

#today
tday = datetime.date.today()
# print(tday.year)
# print(tday.month)
# print(tday.weekday())
# week day monday 0 sunday 6

tdelta = datetime.timedelta(days=7)

#date2 = date1 + timedelta
# timedelta = date1 + date2
bday = datetime.date(2020, 8, 28)
till_bday = bday - tday
print(till_bday.days)
#total.seconds()