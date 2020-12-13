num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
print(f'Essa lista tem {len(num)} elementos' )
num.insert(2, 2)
num.pop()
print(num)
num.pop(2)
print(num)
num.remove(2)
print(num)