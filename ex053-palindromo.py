frase = str(input('Digite ma frase: \n')).strip().upper()
print(frase)
palavras = frase.split() #metodo split transforma a strng em uma lista tendo espaço como separador dos itens da lista
print(palavras)
junto = ''.join(palavras) #metodo 'join' separa as strings com o simbolo indicado entre as aspas
print(junto)
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1): #metodo len define o total de caracteres da string
    inverso = inverso + junto[letra]'''
print(junto, inverso)
if inverso == junto:
    print('Temos uma palídromo! ')
else:
    print('A frase digitada não é um palindromo.')