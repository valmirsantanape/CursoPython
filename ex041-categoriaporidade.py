from datetime import date
nasc = int(input('Digite seu ano de nascimento:  \n'))
anoatual = date.today().year
idade = anoatual - nasc
if idade <= 9:
    print('Idade: {}'.format(idade))
    print('Mirim')
elif idade <= 14:
    print('Idade: {}'.format(idade))
    print('Infantil')
elif idade <= 19:
    print('Idade: {}'.format(idade))
    print('Junior')
elif idade <= 25:
    print('Idade: {}'.format(idade))
    print('Senior')
else:
    print('Idade: {}'.format(idade))
    print('Master')