print('Descubra a area da sua parede e saiba quantas latas  de são necessárias para pinta-las')
alt = float(input('Qual a altura da parede em metros: '))
larg = float(input('Qual a largura da parede em metros '))
area = alt*larg
print('\nA altura da parede é de {} metros'.format(alt))
print('A largura da parede é {} metros '.format(larg))

print('A Area da sua parede corresponde a {}m² '.format(area))

latas = area/2
print('\n \nSerão necessário {} latas de tinta para pintar uma parede cuja a area corresponde a {}m². '.format(latas, area))