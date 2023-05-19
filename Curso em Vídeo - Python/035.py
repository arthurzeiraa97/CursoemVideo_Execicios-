import math as mt
a = float(input('Digite o valor de um dos lados do triângulo: '))
b = float(input('Digite o valor de outro lado do triângulo: '))
c = float(input('Digite o valor do terceiro lado do triângulo: '))
x = b-c
if a < b + c and a > mt.fabs(x):
    print('SUCESSO! Esses três segmentos podem formar um triângulo!')
else:
    print('NÃO VAI ROLAR! Esses três segmentos não podem formar um triângulo!')
