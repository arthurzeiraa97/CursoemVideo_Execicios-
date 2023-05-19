print('~' * 32)
print('    Sequência de Fibonacci')
print('~' * 32)
n = int(input('Quantos termos você quer mostrar? '))
i = 0
a1 = 0
a2 = 1
an = 0
while i < n:
    print(an, end=' -> ')
    i+= 1
    a1 = a2
    a2 = an
    an = a1 + a2
print('FIM')
