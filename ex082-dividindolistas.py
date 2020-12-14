listaprimaria = []
listapar = []
listaimpar = []
while True:
    num = input('Digite um valor ou N para sair: ')
    if num in 'Nn':
        break
    num = int(num)
    while num in listaprimaria:
        print('Numeros duplicados não podem ser adcionados a lista. ')
        num = input('\nDigite um valor ou N para sair:: ')
        if num in 'Nn':
            break
        else:
            num = int(num)
    listaprimaria.append(num)
    if num % 2 == 0:
        listapar.append(num)
        print('paar adcionado')
    else:
        listaimpar.append(num)
        print('impar adcionado')
print()
print('=-' * 30)
print(f'Lista primaria em ordem crescente: {listaprimaria}')
print(f'Lista de numeros pares ordem crescente: {listapar}')
print(f'Lista de numeros impares ordem crescente: {listaimpar}')
print('=-' * 30)