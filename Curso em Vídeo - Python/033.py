n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite mais um valor: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
        menor = n3
maior = n2
if n1>n2 and n1>n3:
    maior = n1
if n3>n2 and n3>n1:
    maior = n3
print('o maior valor é o {} e o menor é o {}!'.format(maior,menor))

