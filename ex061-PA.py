print('------ PROGRESSÃO ARITMÉTICA ------')
a1 = int(input('Digite o prmeiro term da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
n = int(input('Digite quantos termos tera sua PA: '))
c = 0
if razao == 0:
    print('PA Constante')
if razao < 0:
    print('PA decrescente')
else:
    print('PA crescente')
print('PA = {',end='')
while c != n:
    print('{}'.format(a1),end='')
    print(', 'if c < n - 1 else '',end='')
    a1 += razao
    c += 1
print('}')