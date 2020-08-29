ano = int(input('Digite o ano que deseja analisar: '))
if ano % 4 == 0:
    print('O ano de {} é um ano bissexto '.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
