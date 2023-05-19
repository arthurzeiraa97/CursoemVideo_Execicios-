i = 0
lista = []
while True:
    n = int(input('Digite um valor: '))
    i += 1
    lista.append(n)
    lista.sort(reverse=True)
    opcao = str(input('Voce quer continuar? [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Input incorreto...\nDigite somente [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Voce digitou {i} números!')
print(f'Os valores em ordem decrescente são -> {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado e apareceu {lista.count(5)} vezes!')
else:
    print('O valor 5 não fo encontrado na lista!')
