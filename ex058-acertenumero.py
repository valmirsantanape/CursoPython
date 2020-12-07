from time import sleep
from random import randint
sorteio = randint(1, 10)
escolha = int(input('Escolha um numero entre 1 e 10: \n'))
print('Sorteando...')
sleep(1.5)
while escolha != sorteio:
    if escolha < sorteio:
        escolha = int(input('Mais... Você errou! \n'
                            'Esclha outro numero! '))
        print('Sorteando...')
        sleep(1.5)
    else:
        escolha = int(input('Menos... Você errou! \n'
                            'Esclha outro numero! '))
        print('Sorteando...')
        sleep(1.5)
print("Parabens!")