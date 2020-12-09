valor = int(input('Quanto deseja sacar? '))
nota1 = nota10 = nota20 = nota50 = 0
while valor > 0:
    if valor < 10:
        nota1 += 1
        valor = valor - 1
    if valor >= 10:
        nota10 += 1
        valor = valor - 10
    if valor >= 20:
        valor = valor - 20
        nota20 += 1
    if valor >= 50:
        valor = valor - 50
        nota50 += 1
print(f'Notas de 1: {nota1}\n'
      f'Notas de 10: {nota10}\n'
      f'Notas de 20: {nota20}\n'
      f'Notas de 50: {nota50}')