d = float(input('Qual a distância em km que você vai viajar? '))
if d <= 200:
    p1 = 0.5*d
    print('Sua viajem vai custar R${:.2f}!'.format(p1))
else:
    p2 = 0.45*d
    print('Sua viajem vai custar R${:.2f}!'.format(p2))
print('TENHA UMA BOA VIAJEM')
