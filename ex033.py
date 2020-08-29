pimeirovalor = int(input('Digite o primeirovalor: '))
segundovalor = int(input('Digite o segundo valor: '))
terceirovalor = int(input('Digite o terceiro valor: '))

if pimeirovalor > segundovalor and pimeirovalor > terceirovalor:
    print('O maior valor digitado foi ', pimeirovalor)

    if segundovalor > terceirovalor:
        print('O menor valor digitado foi ', terceirovalor)
    else:
        print('O menor valor digitado foi ', segundovalor)

elif segundovalor > terceirovalor:
    print('O maior valor digitado foi ',segundovalor)

    if pimeirovalor > terceirovalor:
        print('O menor valor digitado foi ', terceirovalor)
    else:
        print('O menor valor digitado foi ', pimeirovalor)

else:
    print('O maior valor digitado foi ',terceirovalor)

    if pimeirovalor > segundovalor:
        print('O menor valor digitado foi ', segundovalor)
    else:
        print('O menor valor digitado foi ', pimeirovalor)