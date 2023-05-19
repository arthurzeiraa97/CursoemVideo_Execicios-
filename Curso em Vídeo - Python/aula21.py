#  funçoes parte II

#  interactive help
help(print())
print(print.__doc__)


#  DOCSTRINGS
def contador(i, f, p):
    """
    -> Faz uma contagem de i até f com o passo p e mostra na tela, na qual:
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(c, end=' -> ')
        c += p
    print("FIM!")


contador(0, 100, 10)
help(contador)


#  PARAMETROS OPCIONAIS
def somar(a=0, b=0, c=0):  # agora eu posso informar, ou nao, os 3 parametros
    c = a + b + c
    print(f'A soma vale {c}!')


somar(5, 3)
somar(1)


#  ESCOPO DE VARIÁVEIS
def func(n2):
    global n1
    n1 = 8
    n2 += 3
    print(f'n1 local vale {n1}')
    print(f'n2 local vale {n2}')


n1 = 4  # usando o comando global n1, esse n1 de fora só altera o valor do n2
func(n1)
print(f'n1 global vale {n1}')


#  RETORNO DE VARIÁVEIS
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(1, 2, 3)
r2 = soma(34, 2, 3)
r3 = soma(1, 3)
print(f'Os resultados das somas foram {r1}, {r2} e {r3}')


#  EXEMPLO:
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input("Informe um número: "))
if par(n):
    print("É par!")
else:
    print("É ímpar!")
