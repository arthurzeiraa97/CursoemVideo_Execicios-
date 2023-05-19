from time import sleep
x1 = float(input('Digite o primeiro valor: '))
x2 = float(input('Digite o segundo valor: '))
sleep(0.75)
n = 1
while n != 5:
    print(
        'Você tem as seguintes opções:\n    [1] SOMAR\n    [2] MULTIPLICAR\n    [3] MAIOR\n    [4] NOVOS NÚMEROS\n    [5] SAIR DO PROGRAMA')
    n = int(input('O que você quer fazer? '))
    if n == 1:
        print('A soma entre {} e {} é {:.2f}!'.format(x1,x2,x1+x2))
        print('-='*20)
        sleep(1)
    if n == 2:
        print('A multiplicação entre {} e {} vale {:.2f}!'.format(x1,x2,x1*x2))
        print('-=' * 20)
        sleep(1)
    if n == 3:
        if x1 > x2:
            print('Entre os dois valores informados, o número {} é maior que o {}.'.format(x1,x2))
            print('-=' * 20)
            sleep(1)
        elif x2 > x1:
            print('Entre os dois valores informados, o número {} é maior que o {}.'.format(x2,x1))
            print('-=' * 20)
            sleep(1)
        else:
            print('Os dois valores são iguais!')
            print('-=' * 20)
            sleep(1)
    if n == 4:
        sleep(1)
        x1 = float(input('Digite o primeiro valor: '))
        x2 = float(input('Digite o segundo valor: '))
        print('-=' * 20)
    if n > 5 or n == 0:
        print('Opção inválida! Digite novamente...')
        sleep(1)
        #x1 = float(input('Digite o primeiro valor: '))
        #x2 = float(input('Digite o segundo valor: '))
print('Obrigado por utilizar o programa, te vejo mais tarde!')
