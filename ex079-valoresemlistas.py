from time import sleep
lista = list()
while True:
    num = int(input("Digite um valor  "))
    while num in lista:
        print('Valores dupliados não podem ser adionados...')
        num = int(input("Digite um valor  "))
    sleep(1)
    lista.append(num)
    print('Valor adicinado com sucesso')
    resp = str(input('Deseja continuar? [s/N] '))
    if resp in "Nn":
        break
lista.sort()
print('-_' * 30)
print(f'O valores digitados em ordem crescente foram {lista}')
print('-_' * 30)
