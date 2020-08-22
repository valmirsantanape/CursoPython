resp = 's'
while(resp == 's'):
    numero = int(input('Digie um numero entre 0 e 9999: '))
    if numero < 1:
        print('Digite um numer inteiro!')
    u = numero // 1 % 10
    d = numero // 10 % 10
    c = numero // 100 % 10
    m = numero // 1000 % 10


    if m < 1 and c < 1 and d < 1:
        print('Unidade: ', u)
#       print('Não dezena ')
#       print('Não tem centena')
#       print('Não tem milhar')
    elif m < 1 and c < 1:
        print('Unidade: ', u)
        print('dezena ', d)
#       print('Não tem centena')
#       print('Não tem milhar')
    elif m < 1:
        print('Unidade: ', u)
        print('dezena ', d)
        print('centena',c)
#       print('Não tem milhar')
    else:
        print('Unidade: ', u)
        print('dezena ', d)
        print('Centena', c)
        print('Milhar', m)
    resp = input('Deseja continuar? s/n \n')
print('Obrigado por usar nosso sistema. \n'
      'Até mais!')