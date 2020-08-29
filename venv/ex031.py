distancia = float(input("Qual d distancia total"))
print('Sua viagem vai durar {}km. '.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preco da sua passagem sera de {:.2f}'.format(preco))