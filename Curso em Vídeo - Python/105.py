def notas(*n, sit=False):
    """
    :param n: Uma ou mais notas de alunos
    :param sit: Para mostrar ou nao se a situalao é BOA, RAZOAVEL ou RUIM.
    :return: retorna os parametros MEDIA, MAIOR NOTA, MENOR NOTA, TOTAL DE NOTAS e SITUAÇAO
    """
    lista = {'Média': sum(n) / len(n),
             'Maior nota': max(n),
             'Menor nota': min(n),
             'Total': len(n)}
    if sit:
        if lista['Média'] >= 7:
            lista['Situação'] = 'BOA'
        elif 5.5 <= lista['Média'] < 7:
            lista['Situação'] = 'RAZOÁVEL'
        else:
            lista['Situação'] = 'RUIM'
    return lista


print(notas(6, 8.5, 9.6, 10, 6.78, sit=True))
help(notas)
