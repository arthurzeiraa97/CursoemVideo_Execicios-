s = 0
i = 0
for c in range(3,501,3):
    if c % 2 != 0:
        s = s + c
        i = i + 1
print('A soma de todos os {} valores vale {}!'.format(i, s))
