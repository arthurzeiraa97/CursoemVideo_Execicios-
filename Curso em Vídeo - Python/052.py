n = int(input('Digite um número: '))
i = 0
for c in range(1,n+1):
    if n % c == 0:
        i = i + 1
        print('\033[31m{}'.format(c), end=' ')
    else:
        print('\033[36m{}'.format(c), end=' ')

if i == 2:
    print('\n\033[mO número {} foi divisível {} vezes, por isso ele é PRIMO!'.format(n, i))
else:
    print('\n\033[mO número {} é divisível {} vezes, logo NÃO é primo!'.format(n, i))

