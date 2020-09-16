preco = float(input('Preço do produto: \n'))
avista = preco - preco * 0.10
avistacartao = preco - preco * 0.05
duasvezes = preco
tresvezes = preco + preco * 0.20
forpag = int(input(
      'Avista               [1]\n'
      'Avista cartão        [2]\n'
      'Até 2x no cartao     [3]\n'
      'em até 3x ou mais    [4]\n'))
if forpag == 1:
    print('Valor: R${:.2f}'.format(avista))
elif forpag == 2:
    print('Valor: R${:.2f}'.format(avistacartao))
elif forpag == 3:
    print('Valor: R${:.2f}'.format(duasvezes))
elif forpag == 4:
    print('Valor: R${:.2f}'.format(tresvezes))
else:
    print('Numero inválido.\n'
          'Refaça a operação!')


#Exercício Python 44: Elabore um programa que calcule o valor a ser
# pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros