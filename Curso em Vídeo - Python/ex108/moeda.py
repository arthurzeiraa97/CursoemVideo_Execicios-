def aumentar(x, y=10):
    resp = (1 + y/100)*x
    return resp


def dobro(x):
    resp = 2*x
    return resp


def metade(x):
    resp = x/2
    return resp


def diminuir(x, y=10):
    resp = (1 - y/100)*x
    return resp


def moeda(valor=0, currency="R$"):
    return f'{currency}{valor:.2f}'.replace('.', ',')
