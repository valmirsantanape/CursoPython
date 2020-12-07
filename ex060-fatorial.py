from math import factorial
num = int(input('Digite um numero e descubra seu fatorial: \n'))
fat = factorial(num)
c = num
print('{}! ='.format(num), end=' ')
while c > 0:
    print('{} '.format(c), end='')
    print('*' if c > 1 else '=', end=' ' )
    c -= 1
print(fat)