lista = []
for i in range(0, 5):
    lista.append(int(input(f'Digite o número na posição {i}: ')))
print(f'Você digitou os números -> {lista}')
print(f'O maior valor digitado foi o {max(lista)} na posição(s)', end=' ')
for pos, num in enumerate(lista):
    if num == max(lista):
        print(pos, end='...')
print(f'\nO menor valor digitado foi o {min(lista)} na posição(s)', end=' ')
for count, n in enumerate(lista):
    if n == min(lista):
        print(count, end='...')
