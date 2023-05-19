matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Informe o valor [{i}, {j}]: ')))
print('#' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]:^4}', end='  ')
    print()
print('#' * 30)
