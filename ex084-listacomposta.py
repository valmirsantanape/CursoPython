temp = []
pessoas = list()
mairpeso = 0
menorpeso = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mairpeso = menorpeso = temp[1]
    else:
        if temp[1] > mairpeso:
            mairpeso= temp[1]
        if temp[1] < menorpeso:
            menorpeso = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Deseja coninuar? S/N')).upper()
    if( resp in 'Nn'):
        break
print('=-' * 20)
print(f'{len(pessoas)} pessoas foram cadastradas')
print(f'Dados cadastrados: \n{pessoas}')
print()
print(f'O maior peso foi de {mairpeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mairpeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorpeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ',end='')