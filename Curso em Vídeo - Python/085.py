"""valores = []
pares = []
impares = []
for i in range(1, 8):
    x = int(input(f'Digite o {i}° valor: '))
    valores.append(x)
print('-=' * 30)
for v in valores:
    if v % 2 == 0:
        pares.append(v)
        pares.sort()
    else:
        impares.append(v)
        impares.sort()
print(f'Os valores pares digitados foram -> {pares}')
print(f'Já os ímpares digitados foram -> {impares}')
print('-=' * 30)"""
valores = [[], []]
for i in range(1, 8):
    x = int(input(f'Digite o {i}° valor: '))
    if x % 2 == 0:
        valores[0].append(x)
    else:
        valores[1].append(x)
valores[0].sort()
valores[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram -> {valores[0]} ')
print(f'Os valores ímpares digitados foram -> {valores[1]}')
print('-=' * 30)
