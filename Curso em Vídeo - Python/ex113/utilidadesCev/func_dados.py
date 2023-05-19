def leiaDindin(txt):
    while True:
        num = str(input(txt)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[1;31mERRO! "{num}" é uma entrada inválida\033[0m')
        else:
            return float(num)


def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Entrada inválida.\033[0m')
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de dados interrompida!\033[0m')
            return 0
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            x = float(input(txt))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de dados interrompida!\033[0m')
            return 0
        else:
            return x
