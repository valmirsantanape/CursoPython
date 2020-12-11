from random import randint
num = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(num)
print(f'O maior numero sorteado foi {max(num)}')
print(f'E o menor numero sorteado foi {min(num)}')