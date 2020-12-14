from time import sleep
numeros = list()
print('<>' * 30)
for c in range(1, 6):
    num = int(input('Digite um valor: '))
    if c == 1 or num >= numeros[-1]: #se o numero dcionado for igual a 1 ou maior qe o ultimo adcionar novo item a lista
        numeros.append(num)
        print(f'Numero adcionado na ultima posicao da lista ', numeros)
    else:
        pos = 0
        while True: #enquanto 'pos' for menor que o total de itens na lista faça:
            if num < numeros[pos]: #e se num for menor que o item da lista indexado com o valor "pos"
                numeros.insert(pos, num) #inserir numero na poscao "pos"
                print(f'numero {num} adcionado na posicao {pos} da lista ', numeros)
                break #break para parar o lao while e voltar para o laço for
            print(f'{num}  é maior que o numer da posiçao {pos}')
            pos += 1
            sleep(0)
print('<>' * 30)
print(f'Os valores digitados em ordem foram {numeros}')
print('<>' * 30)
