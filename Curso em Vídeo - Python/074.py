from random import randint
num = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(n, end=' ')
#lista = sorted(num)
#print(f'\nO maior valor vale {lista[4]}\nO menor vale {lista[0]}')
#ou
print(f'O maior valor foi {max(num)}\nO menor foi {min(num)}')
