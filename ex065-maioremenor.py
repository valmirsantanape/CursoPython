num = int(input('Digite um numero?'))
resp = 's'
tot = soma = maior = menor = 0
while resp in "Ss":
    tot = tot + 1
    soma = soma + num
    if tot == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja contnuar? [S/N]')).strip().upper()[0]
    if resp in 'Ss':
        num = int(input("Digite outro numero: "))

media = soma/tot
print('Total de numeros digitados: {}'.format(tot))
print('Média: {} '.format(media))
print('O maior numero digitado foi: {}\n'
      'O menor numero digitado foi: {}'.format(maior, menor))