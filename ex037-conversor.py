numero = int(input('Digite o numro inteiro que deseja converter '))

escolha = int(input('Digite 1 para binário\n'
                    'Digite 2 para octal \n'
                    'Digite 3 para hexadecimal\n'
                    '>>>>'))
if escolha == 1:
    print('Binário')
elif escolha == 2:
    print('Octal')
elif escolha == 3:
    print('Hexadecimal')
else:
    print('Escolha inválida ')