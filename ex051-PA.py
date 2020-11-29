#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input('Digite o primeiro termo da sua prograssão aritmética: \n'))
razao = int(input('Informe qual a razão da PA: '))
n = int(input('Digite o numero de termos da sua PA'))

for c in range(1, n + 1):
    print('{}'.format(a1), end=' ')
    a1 = a1 + razao
print('\nACABOU!')