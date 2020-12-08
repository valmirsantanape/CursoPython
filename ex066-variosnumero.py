tot = soma = 0
while True:
    num = int(input('Digite um numero [Digite 999 para parar]:'))
    if num == 999:
        break
    else:
        tot = tot + 1
        soma = soma + num
print(f'O total de numeros digitados foram {tot}.')
print(f'A soma dos numeros digitados é igual a {soma}.')