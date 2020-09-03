nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Sua média foi de {} pontos. \n'
          'Parabens! Aprovado!'.format(media))
elif media < 7 and media >= 5:
    print('Sua média foi de {} pontos. \n'
          'Você esta na final.'.format(media))
else:
    print('Sua média foi de {} pontos \n'
          'Reprovado!'.format(media))
