print('\033[4:31:40mOlá! Eu vou ler e comparar dois números que você digitar abaixo!\033[m')
x1 = int(input('Digite o primeiro número: '))
x2 = int(input('Digite o segundo número: '))

if x1 > x2:
    print('O número {} é maior que o {}!'.format(x1,x2))
elif x2 > x1:
    print('O número {} é maior que o {}!'.format(x2,x1))
elif x1 == x2:
    print('Os números {} e {} são iguais!'.format(x1,x2))
    