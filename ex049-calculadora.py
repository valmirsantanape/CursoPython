from time import  sleep
print('=-=' * 10)
print('|     TABUADA DE SOMAR       |')
print('=-=' * 10)
num =   int(input('Escolha o numero que deseja somar: \n'))
soma = 0
for c in range(1, 11):
    soma = num + c
    sleep(1)
    print(num ,' + ', c ,' = ',soma)