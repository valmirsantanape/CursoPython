maisvelho = 0
maisnovo = 0
somaidade = 0
media = 0
for pess in range(1, 4):
    print('------ {}º Pessoa -------'.format(pess))
    nome = str(input('nome: '))
    sexo = str(input('Sexo [M/F] : '))
    idade = int(input('Idade: '))
    somaidade += idade
media = somaidade / 3

print('A média de idade do grupo é de {} anos.'.format(media))