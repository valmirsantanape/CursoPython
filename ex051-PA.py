#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
cont = 0
a1 = int(input('Digite o primeiro termo da sua prograssão aritmética: \n'))
razao = int(input('Informe qual a razão da PA: '))
for c in range(1, 11):
    print(a1)
    a1 = a1 + razao