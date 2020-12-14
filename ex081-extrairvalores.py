numeros = list()
totnumeros = 0
posi = 0
print('=-' * 30)
while True:
    num = int(input('Digite um valor: '))
    while num in numeros:
        print(f'Valores duplicados não podem ser adcionado a lista. ')
        num = int(input('Digite um valor: '))
    if posi == 0 or num >= numeros[-1]:
        numeros.append(num)
        print(f'Numero {num} adcionao na ultima posição')
        totnumeros += 1
        posi += 1
    else:
        pos = 0
        while True:
            if num < numeros[pos]:
                numeros.insert(pos, num)
                totnumeros += 1
                break
            print(f'{num}  é maior que o numer da posiçao {pos}')
            pos += 1
    resp = str(input('Quer continuar? [S/N] '))
    if resp not in "S":
        break
pos = 0
while pos < len(numeros):
    if numeros[pos] == 5:
        break
    pos += 1
print()
print('=-' * 30)
if 5 not in numeros:
    print(f'Na lista digitada não exite o numero 5.')
else:
    print(f"O valor 5 esta na posição {pos + 1} lista")
print(f'Os valores digitados foram: {numeros}')
print(f'Foram adcionados {totnumeros} numeros a lista')
print('=-' * 30)
