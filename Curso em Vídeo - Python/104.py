def leiaInt(txt):
    print('-=' * 30)
    num = str(input(txt)).strip()
    while True:
        if num.isnumeric():
            return f'{int(num)}'
        else:
            num = str(input("\033[1;31mERRO!\nDigite um número inteiro válido: \033[0;0m"))


#  Main:
n = leiaInt("Digite um número: ")
print(f'Você digitou o número {n}.')
