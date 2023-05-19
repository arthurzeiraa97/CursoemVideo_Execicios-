import random
import time
numeros = []
print('+-' * 20)
print(f'{"MEGA SENA SORTEADA":^40}')
print('+-' * 20)
n = int(input('Quantos jogos você quer que eu sorteie? ->  '))
time.sleep(1)
print('-=' * 3, 'Anote os seguintes jogos:', '-=' * 3)
time.sleep(1)
for i in range(n):
    while len(numeros) != 6:
        x = random.randint(0, 60)
        if x not in numeros:
            numeros.append(x)
    numeros.sort()
    print(f'Jogo {i+1}: {numeros}')
    time.sleep(1)
    numeros.clear()
print(f'{" < BOA SORTE! > ":=^40}')
