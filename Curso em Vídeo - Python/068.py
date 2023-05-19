from random import randint
print('-=-'*15)
print('         VAMOS JOGAR PAR OU ÍMPAR!')
print('-=-'*15)
i = 0
while True:
    x = int(input('Digite um valor: '))
    c = randint(0,100)
    n = ' '
    while n not in 'PI':
        n = str(input('Par[P] ou Ímpar[I]? ')).upper().strip()[0]
    soma = c + x
    if soma % 2 == 0:
        if n == 'P':
            i += 1
            print('---' * 15)
            print(f'Você jogou {x} e o computador {c}! A soma é {soma} portanto PAR')
            print('---' * 15)
            print('Você VENCEU!\nVamos jogar novamente...')
            print('-=-' * 15)
        else:
            if i == 0:
                print('GAME OVER! JÁ GANHEI DE VOCÊ NA PRIMEIRA HEHEHE')
                break
            else:
                print(f'GAME OVER! Você me venceu {i} vezes seguidas.. Mas agora eu ganhei!')
                break
    if soma % 2 != 0:
        if n == 'I':
            i += 1
            print('---' * 15)
            print(f'Você jogou {x} e o computador {c}! A soma é {soma}, portanto ÍMPAR!')
            print('---' * 15)
            print('Você venceu!\nVamos jogar novamente... ')
            print('-=-' * 15)
        else:
            if i == 0:
                print('GAME OVER! JÁ GANHEI DE VOCÊ NA PRIMEIRA HEHEHE')
                break
            else:
                print(f'GAME OVER! Você me venceu {i} vezes seguidas.. Mas agora eu ganhei!')
                break
