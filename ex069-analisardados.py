resp = 'S'
dezoitoanos = homens = mulheresmenosde20 = 0
while resp in 'S':
    print('=-' * 20)
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: '))
    idade = int(input('Idade: '))
    if sexo in 'Mm':
        if idade == 18:
            dezoitoanos += 1
        homens += 1
    else:
        if idade < 20:
            mulheresmenosde20 += 1
    resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
print('=-' * 20)
print(f'Neste grupo de pessoas {homens} foram cadastrados homens. Destes {dezoitoanos} tem 18 anos. \n'
      f'Neste mesmo grupo há também {mulheresmenosde20} mulheres com menos de 20 anos.')
