sexo = str(input('Digite o seu sexo [F/M]\n ')).strip().upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe o sexo corretamente [F/M]:\n ')).strip().upper()
if sexo == 'F':
    print('Você é do sexo feminino.')
else:
    print('Você é do sexo masculino.')