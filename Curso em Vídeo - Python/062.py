from time import sleep
print('=-='*6)
print('  Gerador de PA')
print('=-='*6)
sleep(1)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão da PA? '))
i = 0
c = a1
n = 10
total = 0
while n != 0:
    total = total + n
    while i < total:
        print('{}'.format(c), end=' -> ')
        c = c + r
        i = i + 1
    print('PAUSA', end=' ')
    n = int(input('\nQuantos termos você quer mostrar a mais? '))
print('\nProgressão finalizada com {} termos mostrados!'.format(total))
