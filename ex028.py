from random import randint
from time import sleep
print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar!')
print('-=-' *20)
num = randint(1, 4)
#print(num)
num2 = int(input('Em que numero pensei? \n'))
print('Voce escolheu o numero {}' .format(num2))


print('processando...')
sleep(3)
if num == num2:
    print('Parabens! Você acertou.')
    print('numero pensado: {}'.format(num))
    print('numero escolhido: {}'.format(num2))

else:
    print('Você errou. ')
    print('O numero que pensei foi {}'.format(num))