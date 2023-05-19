from datetime import date
i = 0
x = 0
atual = date.today().year
for c in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        i = i + 1
    else:
        x = x + 1
print('Ao todo temos {} pessoas maiores de idade\nE também temos {} pessoas menores de idade'.format(i,x))
