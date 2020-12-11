times ='São Paulo', 'Atlético-MG', 'Flamengo', 'Gremio', 'Fluminense',\
       'Internacional', 'Palmeiras', 'Santos', 'Ceará', 'Fortaleza', \
       'Corinthinhas', 'Atletico-PR', 'Bahia', 'Bragantino', 'Atletico-GO', \
       'Sport', 'Vasco', 'Coritiba', 'Botafogo', 'Goias'
'''
print(f'O G4 está formado por')
for cont in range(0, 4):
        print(f'{cont + 1}º {times[cont]}')
print(f'\nEnquando os times que estão a zona de rebaixamento são:')
for cont in range(16, 20):
    print(f'{cont + 1}º {times[cont]}')

print('=-' * 20)
print('Segue a ordem alfabetica a lista de todos os times que participam atualmente do campeonato: ')
'''
ordem = sorted(times)
cont = 0
while cont < 20:
    print(cont + 1, ordem[cont])
    cont += 1