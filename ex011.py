salario = float(input('Digite o valor do salario do seu funcionário e saiba qual será o valor após o aumento'
                      ' de 15%: \n'))
novosalario = salario + (salario*0.15)
print('\n Salário atual R$ {:.2f}'
      '\n Novo salário R$ {:.2f} '.format(salario, novosalario))