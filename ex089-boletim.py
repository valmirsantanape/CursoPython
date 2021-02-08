temp = []
listaPrincipal = []
while True:
    temp.append(str(input('Nome do aluno: ')))
    temp.append(float(input(f'Primeira nota do aluno {temp[0]}: ')))
    temp.append(float(input(f'Segunda nota do aluno {temp[0]}: ')))
    listaPrincipal.append(temp[:])
    temp.clear()
    resp = str(input('Desejar cadastrar outro aluno? [S/N] '))
    if resp in 'Nn':
        break
print('=-' * 25)
print()
for c in range(0, len(listaPrincipal)):
    print(f'{listaPrincipal[c][0]}: Primeia nota {listaPrincipal[c][1]} Segunda nota {listaPrincipal[c][2]}')
    print('Media:', (listaPrincipal[c][1] + listaPrincipal[c][2]) / 2)
    print('-' * 45)
print('-=' * 25)