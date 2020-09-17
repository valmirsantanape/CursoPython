from time import sleep
iniciar = str(input('Deseja niciar contagem? S/N\n'))
iniciar = iniciar.upper()
if iniciar == 'S':
    for c in range(10, 0 - 1, -1):
        sleep(1)
        print(c)
    sleep(1)
    print('Feliz ano novo!!')