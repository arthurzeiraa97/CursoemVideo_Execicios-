lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado...Não vou adicionar!')
    opcao = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Entrada inválida...Somente [S/N]: ')).upper().strip()[0]
    if opcao == "N":
        break
lista.sort()
print('-=-' * 20)
print(f'Valores digitados em ordem crescente -> {lista}')
