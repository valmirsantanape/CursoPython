mensagem = 'Hello World!'
nome = input('Digite eu nome: ')
print('É um praze te conhecer, ' + nome)

resp = input('Vamos brinca?  S/N')

if resp == 'S':

    n1 = int(input('Digite um numero'))
    n2 = int(input('Digite outro numero'))
    soma = n1 + n2

    print('A soma dos numeros digitado é: ', soma)
else:
    print('Até mais! ')
print('Fim da execução')
