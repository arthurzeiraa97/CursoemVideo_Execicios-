from time import sleep
c = ('\033[0m',        # sem cor - 0
     '\033[0;30;41m',  # vermelho - 1
     '\033[0;30;42m',  # verde - 2
     '\033[0;30;43m',  # amarelo - 3
     '\033[0;30;44m'   # azul - 4
     )


def ajuda(txt, cor=0):
    titulo(f'Acessando o comando {txt}', 2)
    sleep(1)
    print(c[4], end='')
    help(txt)
    print(c[0], end='')


def titulo(msg, cor=0):
    print(c[cor], end='')
    print('-=' * 25)
    print(f'{msg:^50}')
    print('-=' * 25)
    print(c[0], end='')


while True:
    sleep(1)
    titulo('SISTEMA DE AJUDA', 3)
    n = str(input('Função ou Biblioteca > '))
    sleep(1)
    if n.upper() == 'FIM':
        sleep(1)
        titulo('Obrigado por utilizar a central, até logo!', 1)
        break
    else:
        ajuda(n)

