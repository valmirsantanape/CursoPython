valorproduct = float(input('Digite o valor do produto desejado: '))
desconto = valorproduct - (valorproduct * 0.05)
print("Valor do produto sem desconto R$ {:.2f}\n "
      "Valor do produto com desconto R$ {:.2f} ".format(valorproduct, desconto))