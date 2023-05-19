print('==' * 20)
print(f'{"Listagem de Preços":^40}')
print('==' * 20)
lista = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo',
         '25.00', 'Transferidor', '4.20', 'Compasso', '9.99', 'Mochila', '120.32',
         'Canetas', '22.30', 'Livro', '34.90')
l = 0
p = 1
while True:
    l += 2
    p += 2
    print(f'{lista[l]:.<31}R${lista[p]:>7}')
    if p >= 17:
        break
print('==' * 20)
