from datetime import datetime
trabalhadores = list()
dados = dict()
dados['nome'] = nome = str(input('Digite o nome do empregado: '))
anoNasc = int(input('Digite o ano de nascimento: '))
idade = datetime.now().year - anoNasc
dados['idade'] = idade
dados['ctps'] = int(input(f'Numero da carteira de trabalho (0 não tem) : '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35 - datetime.now().year)
print()
for k, v in dados.items():
    print(f' -  {k}: {v}')

