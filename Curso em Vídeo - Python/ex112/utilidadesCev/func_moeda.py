def aumentar(x, y=10, show=False):
    resp = (1 + y / 100) * x
    if show:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp


def dobro(x, show=False):
    resp = 2 * x
    if show:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp


def metade(x, show=False):
    resp = x / 2
    if show:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp


def diminuir(x, y=10, show=False):
    resp = (1 - y / 100) * x
    if show:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp


def moeda(valor, nota="R$"):
    return f'{nota}{valor:.2f}'.replace('.', ',')


def resumo(x=100, taxa_1=10, taxa_2=10, txt=" "):
    print('-' * 60)
    print(f'{txt:^60}')
    print('-' * 60)
    print(f'Preço analisado:{moeda(x):.>44}')
    print(f'Dobro do preço:{dobro(x, True):.>45}')
    print(f'Metade do preço:{metade(x, True):.>44}')
    print(f'{taxa_1}% de aumento:{aumentar(x, taxa_1, True):.>43}')
    print(f'{taxa_2}% de redução:{diminuir(x, taxa_2, True):.>43}')
    print('-' * 60)
