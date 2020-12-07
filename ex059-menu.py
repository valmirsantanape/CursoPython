num1 = int(input('Informe o primeiro numero :'))
num2 = int(input('Informe o segundo numero :'))
resp = ''
while resp in 'Ss':
    escolha = int(input('Escolha estre as opções: \n'
                            '[1] somar\n'
                            '[2] multiplicar\n'
                            '[3] maior\n'
                            '[4] novos numeros\n'
                            '[5] sair\n'))

    while escolha == 4:
        num1 = int(input('Informe um novo primeiro numero :'))
        num2 = int(input('Informe um novo segundo numero :'))
        escolha = int(input('Escolha estre as opções: \n'
                            '[1] somar\n'
                            '[2] multiplicar\n'
                            '[3] maior\n'
                            '[4] novos numeros\n'
                            '[5] sair\n'))
    if escolha == 1:
        soma = num1 + num2
        print(soma)
    elif escolha == 2:
        mult = num1 * num2
        print(mult)
    elif escolha == 3:
        if num1 > num2:
            print(num1)
        elif num1 == num2:
            print(num1)
        else:
            print(num2)
    elif escolha == 5:
        break
    resp = str(input('Deseja repetir a operação? [S/N]'))
print('Fim do programa!')