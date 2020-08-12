print('-----------------------------------')
print('|        MEDIA DAS NOTAS          |')
print('-----------------------------------')
nota1 = float(input('Digite sua primera nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = ((nota1+nota2)/2)
print('')
print('>> Sua primeira nota registrada foi de {} pontos.\n'
      '>> Sua segunda nota registrada foi de {} pontos. \n'
      '>> Sua média final é de {} pontos'  .format(nota1, nota2, media))
if media >= 6:
    print('\n Parabéns! Você foi aprovado. ')
elif media < 6 and media >= 4:
    print('\n Você esta em recuperação na disiplina avaliada. ')
else:
    print('\n Voce está reprovado. ')