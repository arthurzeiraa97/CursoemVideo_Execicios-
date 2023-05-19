lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        i = 0
        while i < len(lista):
            if n <= lista[i]:
                lista.insert(i, n)
                print(f'Adicionado na posição {i}...')
                break
            i += 1
print(f'Os valores digitados em ordem cescente foram -> {lista}!')
