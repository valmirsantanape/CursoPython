matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPar = somaPar + matriz[l][c]
        somaCol3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-' * 20)
print(f'Soma dos numeros pares: {somaPar}')
print(f'Som dos numeros da terceira coluna: {somaCol3}')