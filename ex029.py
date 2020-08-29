from time import sleep
velocidade = int(input('Informe em km qual a velocidade do veículo\n '))
print('Calculando...')
sleep(2)
print('Veloidade registrada foi de {} km/h' .format(velocidade))
if velocidade > 80:
    print('Você foi multado por ultrapassar a velocidade máxima permitida ')
    print('Valor da multa é de R$280,00 (Duzentos e oitenta reais)\n')
    print('Tenha um bom dia! \nDirija sempre com segurança!')
else:
    print('Tenha um bom dia! \nDirija sempre com segurança!')

