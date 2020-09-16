reta1 = float(input('Digite a primeira reta: \n'))
reta2 = float(input('Digite a primeira reta:\n'))
reta3 = float(input('Digite a primeira reta:\n'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:

    if reta1 == reta2 == reta3:
        print('As retas indicadas podem formar um triângulo equilátero. ')
    elif reta1 != reta3 and reta1 != reta2 and reta2 != reta3:
        print('As retas indicadas podem formar um triângulo escaleno. ')
    else:
        print('As retas indicadas podem formar um triângulo isósceles. ')
else:
    print('A retas indicadas não podem formar um trângulo. ')