frase = 'Curso em Video Python'
print('Manipulando String')

print(frase[9])
print(frase[9:14])
print(frase[9:20:2])
print(frase[15:])
print(frase[:5])

print(len(frase))
print('frase.count(','o',') pega a letra indicada no paramentro'
       ' e retorna quantas foram encontradas'
                         '. No exemplo foram encontradas  ',  frase.count('o'),'letras do tipo')
print(frase.find('curso'))
print(frase.replace('Python', "Android"))
print(frase.upper())
print(frase.lower())

print(frase.capitalize())
print(frase.title())
print(frase.strip())
nome = input('Digite seu nome completo')
print(nome)
print('Nome com todas asletras maiusculas', nome.upper())
print('Nome com todas asletras minusculas', nome.lower())
print('Total de caractere considerando os espaços: ', len(nome.strip()))
print('Total de carctere sem considerar os espaços: ', len(nome))