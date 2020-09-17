print('Somas dos numeros impares multiplos de 3 entre 0 e 500')
s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))