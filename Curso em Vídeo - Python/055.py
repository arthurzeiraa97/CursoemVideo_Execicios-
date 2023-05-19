i = 0
peso = []
for c in range(1,6):
    peso.append(float(input('Peso da {}ª pessoa em kg: '.format(c))))
peso.sort()
print('O maior peso lido foi {} kg\nJá o menor peso lido foi de {} kg'.format(peso[4],peso[0]))
