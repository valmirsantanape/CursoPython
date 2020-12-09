from random import randint
from time import sleep
par = 0
impar = 1
while True:
    num = int(input('Digite um numero de 0 a 10: '))
    resp = str(input('Impar ou Par? [I/P]'))
    num2 = randint(0, 10)
    sorteio = num + num2
    print(f'Jogador {num}\n'
          f'Computador {num2}')
    sleep(3)
    if resp in "Pp":
        if sorteio % 2 == 0:
            print('Voce acertou')
        else:
            break
    if resp in 'Ii':
        if sorteio % 2 == 0:
            break
        else:
            print('Voce acertou!')