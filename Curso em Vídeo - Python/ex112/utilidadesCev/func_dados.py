def leiaDindin(txt):
    while True:
        num = str(input(txt)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[1;31mERRO! "{num}" é uma entrada inválida\033[0m')
        else:
            return float(num)


def leiaInt(txt):
    print('-=' * 30)
    num = str(input(txt))
    while True:
        if num.isnumeric():
            return f'{int(num)}'
        else:
            num = str(input("\033[1;31mERRO!\nDigite um número inteiro válido: \033[0;0m"))
