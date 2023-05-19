lista = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
    'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    x = int(input('Digite um número entre 0 e 20: '))
    while x > 20 or x < 0:
        x = int(input('Você digitou um número fora do range...\nSomente entre 0 e 20: '))
    print(f'Você digitou o número {lista[x]}!')
    opcao = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Opção incorreta...\nSomente [S/N] para continuar: ')).upper().strip()[0]
    if opcao == 'N':
        break
print('Até logo!')
