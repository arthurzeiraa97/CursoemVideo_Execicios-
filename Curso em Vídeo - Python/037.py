x = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão: ')
print('[1] para BINÁRIO')
print('[2] para OCTAL')
print('[3] para HEXADECIMAL')
n = int(input('Sua opção: '))
if n == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(x, bin(x)))
elif n == 2:
    print('{} convertido para OCTAL é igual a {}'.format(x, oct(x)))
elif n == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(x, hex(x)))

