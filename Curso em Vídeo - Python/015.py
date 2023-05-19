t = float(input('Quantos dias o carro foi alugado?'))
d = float(input('Quantos Km foram percorridos?'))
custo = 60*t + 0.15*d
print('O total a pagar é {:.2f}R$!'.format(custo))
