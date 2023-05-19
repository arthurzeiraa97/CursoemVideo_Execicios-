def fatorial(n=1, show=False):
    """
    :param n: Fatorial a ser calculado
    :param show: True para mostrar a conta, False para mostrar somente o resultado
    :return: Retorna o resultado
    """
    f = 1
    while n > 0:
        if show:
            print(f'{n}', end=' ')
            print(" x " if n > 1 else ' = ', end=' ')
        f *= n
        n -= 1
    return f


print(fatorial(4, show=True))
help(fatorial)
