print('='*30)
print('     10 PRIMEIROS TERMOS DE UMA PA')
print('='*30)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Informe a razão: '))
decimo = a1 + (11 - 1) * r
for c in range(a1,decimo,r):
    print(c, end=' -> ')
print('ACABOU')

