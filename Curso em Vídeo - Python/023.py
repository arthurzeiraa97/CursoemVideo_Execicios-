x = int(input('Digite um valor de 0 a 9999:'))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x//1000 % 10
print('Analisando o valor: {}'.format(x))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))

