lista = []
maior = menor = 0
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0:
        maior = n
        menor = n
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        if n > maior:
            maior = n
            lista.append(n)
            print('Adicionado ao final da lista...')
        elif n < menor:
            menor = n
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista...')
        elif lista[0] < n < lista[1]:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista...')
        elif lista[1] < n < lista[2]:
            lista.insert(2, n)
            print('Adicionado na posição 2 da lista...')
        elif lista[2] < n < lista[3]:
            lista.insert(3, n)
            print('Adionado na posição 3 da lista...')
print(f'Os valores digitados em ordem crescente foram -> {lista}')
