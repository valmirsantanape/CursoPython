nome = input('Digite o nome de uma cidade ')
nome = nome.split()
print(nome[0])

if(nome[0] == 'Santo'):
    print("O nome da sua cidade inicia com a palavra {}" .format('Santo'))
else:
    print("O nome da sua cidade não inicia com a palavra {}".format('Santo') )