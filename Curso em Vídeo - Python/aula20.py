#  funçoes
"""def soma(a, b):
    print(f'A soma entre A = {a} e B = {b} vale:', end=' ')
    s = a + b
    print(s)


#  Main:
soma(int(input("Digite o primeiro valor de a: ")), 4)
soma(1993, 3234)
soma(-2, 6)"""


"""def dobra(lista):
    i = 0
    while i < len(lista):
        lista[i] = lista[i] * 2
        i += 1


valores = [2, 6, 23, 12, 4]
dobra(valores)
print(valores)"""


def soma(*valores):
    s = 0
    for c in valores:
        s += c
    print(f'A soma dos valores {valores} vale {s}')


soma(3, 4, 5, 11)
soma(12, 3)
