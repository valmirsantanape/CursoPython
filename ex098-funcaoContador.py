from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print()
        print('=-' * 30)
    if i > f:
        print(f'Contagem de {i} ate {f} de {p} em {p}')
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print()
        print('=-' * 30)
contador(1, 10, 1)
contador(10, 1, 2)

print(f'                Contagem personalisada')
inicio = int(input(f'Digite o valor que deseja iniciar a contagem: '))
fim = int(input(f'Digite o valor onde deseja terminar a contagem: '))
passo = int(input(f'Digite o valor do passo da sua contagem: '))
contador(inicio, fim, passo)
