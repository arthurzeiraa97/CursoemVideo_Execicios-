soma = 0
i = 0
for c in range(1,7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma = soma + n
        i = i + 1
print('A soma de todos os {} números pares digitados vale {}!'.format(i, soma))
