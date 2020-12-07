print('------ PROGRESSÃO ARITMÉTICA ------')
primeiro = int(input('Digite o prmeiro term da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
n = int(input('Digite quantos termos tera sua PA: '))
if razao == 0:
    print('PA Constante')
if razao < 0:
    print('PA decrescente')
else:
    print('PA crescente')
resp = n
while resp != 0:
    c = 0
    a1 = primeiro
    print('PA = {', end='')
    while c != resp:
        print('{}'.format(a1),end='')
        print(', 'if c < resp - 1 else '',end='')
        a1 += razao
        c += 1
    print('}')
    resp = int(input('(Digite 0 para sair do programa) \nInforme o numero de termos que deseja exibir desta PA?'))
print('Você saiu do programa. ')