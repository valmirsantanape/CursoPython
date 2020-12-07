num1 = int(input('Digte um numro e descubra seu fatorial '))
num2 = num1
#5! = 5*4*3*2*1
fat = 1
while num2 > 0:
    fat = fat * num2
    num2 += -1
print('O fatorial de {} é igual a {}'.format(num1, fat))