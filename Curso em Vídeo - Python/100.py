from random import randint
from time import sleep
valores = list()


def sorteia(lista):
    for i in range(5):
        lista.append(randint(0, 15))
    print('-=' * 30)
    print("Sorteando os 5 valores da lista temos: ", end='')
    sleep(0.75)
    for n in lista:
        print(n, end=' ')
        sleep(0.75)
    print('-> Pronto!')


def soma_par(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares da lista -> {lista} vale {soma}')


#  MAIN:
sorteia(valores)
soma_par(valores)
