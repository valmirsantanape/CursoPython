from math import sqrt, floor

print('Digite os valores dos catetos de um triangulo retangulo e encontre a hipotenusa')
cat1 = float(input('Digite o cateto oposto: \n'))
cat2 = float(input('Digite o cateto adjacente: \n'))


hipotenusa = cat1**2 + cat2**2
print("A hipotenusa do triangulo retangulo especificado é {:.2f}. \n Parte inteira da hipotenusa é {} ".format(sqrt(hipotenusa), floor(sqrt(hipotenusa))))