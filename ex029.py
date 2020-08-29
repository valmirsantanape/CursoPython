from time import sleep
velocidade = int(input('Informe em km qual a velocidade do veículo\n '))
print('Calculando...')
sleep(2)
print('Veloidade registrada foi de {} km/h' .format(velocidade))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado por ultrapassar a velocidade máxima permitida ')
    print('Valor da multa é de R${},00 \n'.format(multa))
    print('Tenha um bom dia! \nDirija sempre com segurança!')
else:
    print('Tenha um bom dia! \nDirija sempre com segurança!')

