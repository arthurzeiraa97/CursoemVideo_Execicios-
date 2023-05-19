lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    opcao = str(input('Voce quer continuar? [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Input inválido...\nVoce quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print('*-' * 30)
print(f'A lista completa digitada foi -> {lista}')
print(f'A lista de pares foi -> {pares}')
print(f'A lista dos ímpares foi -> {impares}')
