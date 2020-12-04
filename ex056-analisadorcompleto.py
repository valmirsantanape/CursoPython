maioridadehomem = 0
maisvelho = 0
maisnovo = 0
somaidade = 0
media = 0
nomevelho = ''
totmulher20 = 0
for pess in range(1, 5):
    print('------ {}º Pessoa -------'.format(pess))
    nome = str(input('nome: ')).strip()
    sexo = str(input('Sexo [M/F] : ')).strip()
    idade = int(input('Idade: '))
    somaidade += idade
    if pess == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))