frase = str(input('Digite uma frase: \n')).strip()
print('A  letra ''''a ''''aparece {} vezes na frase ' .format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição {} ' .format(frase.upper().find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.upper().rfind('A')+1))