print('CONVERÇÃO DE MOEDA ')

valoremreais = float(input('Digite a quantiaem RBL que você deseja converter para USD '))
print(valoremreais)
valoremdolar = valoremreais / 3.27
print('Com R$ {} Você poderá comprar\n'
      ''.format(valoremreais, valoremdolar))