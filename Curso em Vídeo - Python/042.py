x1 = int(input('Primeiro Segmento: '))
x2 = int(input('Segundo Segmento: '))
x3 = int(input('Terceiro Segmento: '))
if x1 + x2 > 3 and x1 + x3 > x2 and x2 + x3 > x1:
    print('Os segmentos PODEM FORMAR um triângulo',end=' ')
    if x1 == x2 == x3:
        print('EQUILÁTERO!')
    elif x1 != x2 != x3 != x1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Esses segmentos NÃO PODEM FORMAR um triângulo!')



