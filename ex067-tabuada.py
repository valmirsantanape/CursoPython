cont = soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num < 0:
        break
    print('------ SOMA -------')
    while cont <= 10:
        soma = soma + num
        print(f'{num} + {cont} = {soma}')
        cont = cont + 1
    print('\n------ SUBTRAIR -------')
    cont = 10
    sub = 0
    while cont >= 0:
        sub = num - cont
        print(f'{num} - {cont} = {sub}')
        cont = cont - 1
    print('\n------ Multiplicar -------')
    cont = mult = 0
    while cont <= 10:
        mult = num * cont
        print(f'{num} x {cont} = {mult}')
        cont = cont + 1
    print('\n------ Dividir -------')
    cont = div = 1
    while cont <= 10:
        if num % cont == 0:
            div = num / cont
            print(f'{num} : {cont} = {div}')
        cont += 1