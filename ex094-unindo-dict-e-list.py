pessoa = dict()
pessoas = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Por favor digite M ou F')).upper()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    resp = str(input('Deseja continuar: '))
    if resp not in 'Ss':
        break
print('-=' * 30)
print(pessoas)
print('-=' * 30)