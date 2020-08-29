from random import randint
from time import sleep
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
nome = [n1,n2,n3,n4]
print('sorteando...')
sleep(3)
num = int(randint(0,3))
print(nome[num])
