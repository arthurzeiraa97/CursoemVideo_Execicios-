def aumentar(x, y=10, show=False):
    print('-=' * 30)
    resp = (1 + y/100)*x
    if show:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp


def dobro(x, show=False):
    resp = 2*x
    if show:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp


def metade(x, show=False):
    resp = x/2
    if show:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp


def diminuir(x, y=10, show=False):
    resp = (1 - y/100)*x
    if show:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp


def moeda(valor=0, currency="R$"):
    return f'{currency}{valor:.2f}'.replace('.', ',')
