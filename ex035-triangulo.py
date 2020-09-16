reta1 = float(input('Digite a primeira reta'))
reta2 = float(input('Digite a primeira reta'))
reta3 = float(input('Digite a primeira reta'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas indicadas podem formar um triângulo. ')
else:
    print('A retas indicadas não podem formar um trângulo. ')