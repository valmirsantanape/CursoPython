alt = float(input('Digite sua altura em cm: \n'))
peso = float(input('Digite seu peso em kg:\n' ))
imc = peso/(2*(alt/100))
print('Seu imc é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')


#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida