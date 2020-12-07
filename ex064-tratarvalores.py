num = 0
soma = 0
tot = 0
while num != 999:
    num = int(input('Digite um nmero [999 para parar]'))
    soma = soma + num
    tot = tot + 1
totsoma = soma - 999
print('O total de numeros digitados foram {}\n'
      'A soma desses numeros é igual a {}'.format(tot - 1, totsoma))
print('FIM')