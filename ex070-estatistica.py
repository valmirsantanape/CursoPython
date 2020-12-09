total = maisbarato = maiorquemil = cont = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    if cont == 1:
        maisbarato = preco
        nomemaisbarato = produto
    else:
        if preco < maisbarato:
            maisbarato = preco
            nomemaisbarato = produto
    if preco > 1000:
        maiorquemil += 1
    total = total + preco
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Total: R${total:.2f}\n'
      f'Produto mais barato: {nomemaisbarato} - R${maisbarato:.2f}\n'
      f'Do total {maiorquemil} produtos estão acima de mil reais')
