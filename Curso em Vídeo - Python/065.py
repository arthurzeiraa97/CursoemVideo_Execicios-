i = 0
soma = 0
n = 's'
maior = 0
menor = 0
while n in 's':
    x = float(input('Informe um número: '))
    i += 1
    soma += x
    if i == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        elif x < menor:
            menor = x
    n = str(input('Voce quer continuar? [s/n]... '))
    if n != str and n != 's' and n != 'n':
        while n != 'n' and n != 's':
            n = str(input('Entrada incorreta! Digite somente s ou n: '))
    '''if n == 'n':
        break'''
    '''while n != str and n != 's':
        n= str(input('Entrada incorreta! Digite somente s ou n: '))
        if n == 'n':
            break'''
media = soma / i
print('Você digitou {} números e a média entre eles foi de {:.2f}!'.format(i, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
