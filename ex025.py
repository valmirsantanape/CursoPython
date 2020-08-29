nome = str(input('Digite seu nome: ')).strip()
nome2 = str(input('Qual nome você deseja encontrar? ')).strip()
print('Seu nome tem {}? ' .format(nome2), nome2.upper() in nome.upper())