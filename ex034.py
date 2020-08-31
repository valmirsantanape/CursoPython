salario = float(input('Digite o salario do funcionário'))
if salario <= 1250:
    salarionovo = salario + (salario * 0.15)
    print('O novo salario do seu funcionário após o ultimo aumento será de '.format(salarionovo))
else:
    salarionovo = salario + (salario * 0.10)
    print('O novo salario do seu funcionário após o ultimo aumento será de '.format(salarionovo))



#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário
#e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule
#um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

