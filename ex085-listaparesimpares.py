listUni = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        listUni[0].append(valor)
    else:
        listUni[1].append(valor)
print('=-' * 30)
print(f'[{listUni}')
listUni[0].sort()
listUni[1].sort()
print(f'Lista dos numeros pares: {listUni[0]}')
print(f'Lista dos numeros impares: {listUni[1]}')
