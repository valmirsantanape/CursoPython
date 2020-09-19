soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um {}º valor: '.format(c)))
    if num% 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Vcê informou {} numeros pares e a soma desses numeros é {}.'.format(cont, soma))
