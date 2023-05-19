# LISTAS
# entre colchetes []
'''lista = [int(input('n1: ')), int(input('n2: ')), int(input('n3: ')), int(input('n4: ')), int(input('n5: '))]
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)
lista.pop()
print(lista)
lista.append(4)
print(lista)
print(min(lista))'''

valores = list()  # ou valores = [] para declarar uma lista vazia
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for p, v in enumerate(valores):
    print(f'Encontrei o {v} na posiçao {p}!')

