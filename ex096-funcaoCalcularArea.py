def area(a, b):
    area = a * b
    print('=-' * 30, end='' '=')
    print(f'\n  A area do terreno com dimenções {a} x {b} metros é de {area}m²')
    print('=-' * 30, end='' '=')
a = int(input('Qual o comprimento do terreno? '))
b = int(input('Qual a largura do terreno? '))
area(a, b)