matriz = [[], [], []]
soma_pares = soma_tercoluna = 0
for i in range(3):
    for j in range(3):
        x = int(input(f'Digite o número para a posição [{i}, {j}]: '))
        if x % 2 == 0:  # soma num pares
            soma_pares += x
        matriz[i].append(x)
for c in range(3):  # soma terceira coluna
    soma_tercoluna += matriz[c][-1]
print('-=' * 25)
for i in range(3):
    for j in range(3):
        print(f'         {matriz[i][j]:^3}', end=' ')  # printando a matriz
    print()
print('-=' * 25)
print(f'A soma entre os números pares da matriz vale {soma_pares}!')
print(f'A soma entre os números da terceira coluna vale {soma_tercoluna}!')
print(f'O maior valor da segunda linha é o {max(matriz[1])}.')
