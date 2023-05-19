from time import sleep
print('=-='*6)
print('  Gerador de PA')
print('=-='*6)
sleep(1)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão da PA? '))
i = 0
c = a1
while i < 10:
    sleep(1)
    print('{}'.format(c),end=' -> ')
    c = c + r
    i = i + 1
print('FIM!',end=' ')
