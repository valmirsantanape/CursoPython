from random import randint
from time import sleep
sorteio = []
temp = []
jogos = int(input('Digite o numero de jogos que deseja fazer: '))
for c in range(0, jogos):
    for i in range(0, 6):
        num = randint(0, 60)
        while num in temp:
            num = randint(0, 60)
        temp.append(num)
    sorteio.append(temp[:])
    temp.clear()
for c in range(0, jogos):
    sorteio[c].sort()
    sleep(2)
    print(f'Sorteio Nº {c + 1} => {sorteio[c]}')
