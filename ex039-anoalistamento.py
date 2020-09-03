from datetime import date
data_atual = date.today().year
ano = int(input('Qual seu ano de nascimento:\n'))
idade = data_atual - ano
rest = 18 - idade
if idade < 18:
    if rest == 1:
        print('Ainda falta {} ano para você completar 18 ano(s) e poder se alistar'.format(rest))
    else:
        print('Ainda faltam {} anos para você completar 18 ano(s) e poder se alistar'.format(rest))
elif idade == 18:
    print('No ano atual você completa 18 anos. \n'
          'Procure ajunta militar mais proxima e se aliste ao serviço militar.')
else:
    if rest == -1:
        print(
            'Seu periodo de alistamento militar iniciou desde o ano de {}, por tanto você esta há {} ano atrasado.\n'
            'Procure a junta militar mais proxima para ficar quite com a justiça militar'.format(data_atual + rest,
                                                                                                 rest * (-1)))
    else:
        print('Seu periodo de alistamento militar iniciou desde o ano de {}, por tanto você esta há cerca de {} anos atrasado.\n'
          'Procure a junta militar mais proxima para ficar quite com a justiça militar'.format(data_atual + rest, rest*(-1)))
