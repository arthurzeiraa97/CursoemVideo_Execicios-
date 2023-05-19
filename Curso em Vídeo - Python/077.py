lista = ('APRENDER', 'AMAR', 'CURSO', 'ESTUDAR', 'PRATICAR', 'FUTURO',
         'CEBOLA', 'CARNE', 'MERCADO')
for i in lista:
    print(f'\nNa palavra {i} temos ', end='')
    for letra in i:
        if letra in 'AEIOU':
            print(letra, end=' ')
