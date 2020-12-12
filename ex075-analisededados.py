num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: ' ))
lista = num1, num2, num3, num4
print(f'O valor 9 apareceu {lista.count(9)} vezes. ')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3)+1}ª posição.')
else:
    print('O numero 3 não existe na lista. ')
print('O numeros pares digitados são: ', end=' ')
for cont in range(0, 4):
   if cont % 2 == 0:
       print(cont, end=' ')
