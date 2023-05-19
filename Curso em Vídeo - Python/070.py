print('='*55)
print('  Informe os seus itens que voce comprou logo abaixo!')
print('='*55)
soma = totmil = i = 0
valorbarato = 0
maisbarato = ' '

while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: R$ '))
    print('=' * 55)
    i += 1
    soma += preco
    if i == 1 or preco < valorbarato:
        valorbarato = preco
        maisbarato = nome
    '''else:
        if preco < valorbarato:
            maisbarato = nome'''
    if preco > 1000:
        totmil += 1
    opcao = str(input('Quer registrar mais algum produto? [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Digitação incorreta...\nQuer registrar mais algum produto? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

print('='*55)
print(f'O valor total da compra foi de R${soma:.2f} e você comprou {totmil} itens acima de R$1000.00\ne o item mais barato da lista foi o(a) {maisbarato}'
      f' que custou R${valorbarato:.2f}!')
