print('CONVERÇÃO DE MOEDA ')

valoremreais = float(input('Digite a quantia em Real Brasileiro(R$) que você deseja converter para Dolares Americano (USD$) '))
print('R${:.2f}' .format(valoremreais))
valoremdolar = valoremreais / 3.27
print('Com R$ {:.2f} Você poderá comprar\n'
      'US$ {:.2f} dolares '.format(valoremreais, valoremdolar))
print('Obrigado por utilizar o sistema.')