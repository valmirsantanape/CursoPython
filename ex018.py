from math import sin, cos, tan, radians
angulo = float(input('Digite a medida do angulo que vc deseja verificar: \n'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno do angulo {} é igual a {:.2f} '.format(angulo, seno))
print('O cosseno do angulo {} é igual a {:.2f} '.format(angulo, cosseno))
print('A tangete do angulo {} é igual a {:.2f} '.format(angulo, tangente))