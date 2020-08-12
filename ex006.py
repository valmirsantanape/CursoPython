print('TABUADA DE UM NUMERO QUALQUER')
num = int(input('Digit o numero: '))
cont = 1

while cont <= 10:
    mult = num * cont
    print(num, '*', cont, '=', mult)
    cont = cont + 1

print('\nFim da execução: ')