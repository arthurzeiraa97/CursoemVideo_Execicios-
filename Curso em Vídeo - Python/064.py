n = int(input('Digite um número inteiro [obs. 999 para parar]: '))
i = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro [obs. 999 para parar]: '))
    i += 1
    soma += n
print('Você digitou {} e a soma deles foi {}!'.format(i,soma))
# print('Você digitou {} e a soma deles foi {}!'.format(i-1,soma-999))
