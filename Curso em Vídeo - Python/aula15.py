# comando break
n = s = 0
while True:
    n = int(input('Informme um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
print(f'A soma vale {s}!')
# formataçao de numeros
print(f'A soma vale {s:.2f}')
