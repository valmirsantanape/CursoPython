from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i + 1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    ocp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if ocp == 999:
        print('FINALIZANDO', end='')
        for c in range(1, 4):
            print('.', end='')
            sleep(1)
        print()
        break
    if ocp <= len(ficha) - 1:
        print(f'Notas de {ficha[ocp][0]} são {ficha[ocp][1]}')
print('<<< VOLTE SEMPRE >>>')