numeros = list()
for pos, c in enumerate(range(1, 6)):
    num = int(input(f'Digite um valor para a posição {pos}: '))
    numeros.insert(pos, num)
print(numeros)