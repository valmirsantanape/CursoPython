from time import sleep
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
'''for pos, cont in enumerate(contagem):

    print(f'{pos} {cont}')
    sleep(1)
'''
res = 'S'
while res in 'S':
    num = int(input('Digie um numero entre 0 e 20: '))
    print(f'{num} - {contagem[num]}')
    res = str(input('Deseja continuar? [S/N] ').strip().upper()[0])