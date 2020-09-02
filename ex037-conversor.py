numero = int(input('Digite o numro inteiro que deseja converter '))

escolha = int(input('Digite 1 para binário\n'
                    'Digite 2 para octal \n'
                    'Digite 3 para hexadecimal\n'
                    '>>>>'))
if escolha == 1:
    print('O numero {} convertido para binário é {}.'.format(numero, bin(numero)))
elif escolha == 2:
    print('O numero {} convertido para octal é {}.'.format(numero, oct(numero)))
elif escolha == 3:
    print('O numero {} convertido para hexdecimal é {}.'.format(numero, hex(numero)))
else:
    print('Escolha inválida ')