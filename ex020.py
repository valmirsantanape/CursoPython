from random import shuffle
al1 = input('Primeiro Aluno: ')
al2 = input('Segundo Aluno: ')
al3 = input('Terceiro Aluno: ')
al4 = input('Quarto Aluno: ')
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentacao será: ')
print(lista)