from time import sleep
from random import randint
print('PEDRA, PAPEL, TESOURA')
lista =['PEDRA', 'PAPEL', 'TESOURA']

escolha = int(input('[0] PEDRA\n'
                    '[1] PAPEL\n'
                    '[2] TESOURA\n'))

jogador = lista[escolha]
#sleep(1)
print('JO')
#sleep(1)
print('KENN')
#sleep(1)
print('POO')

computer = randint(0, 2)
maquina = lista[computer]


if escolha == computer:
    print('Empate')
elif escolha == 0 and computer == 2:
    print('Voce: {} X Computador: {}'.format(jogador, maquina))
    print('Você venceu')
elif escolha == 0 and computer == 1:
    print('Voce: {} X Computador: {}'.format(jogador, maquina))
    print('Voce perdeu')
elif computer == 0 and escolha == 2:
    print('Voce: {} X Computador: {}'.format(jogador, maquina))
    print('Voce perdeu')
elif computer == 0 and escolha == 1:
    print('Voce: {} X Computador: {}'.format(jogador, maquina))
    print('Você venceu')
elif computer == 1 and escolha == 2:
    print('Voce: {} X Computador: {}'.format(jogador, maquina))
    print('Voce venceu')
elif computer == 2 and escolha == 1:
    print('Voce: {} X Computador: {}'.format(jogador, maquina))
    print('Voce perdeu')
elif escolha == 1 and computer == 2:
    print('Voce: {} X Computador: {}'.format(jogador, maquina))
    print('Você venceu')
elif escolha == 2 and computer == 1:
    print('Voce: {} X Computador: {}'.format(jogador, maquina))
    print('Você venceu')