import moeda

n = float(input("Digite um valor: R$ "))
taxa = float(input("Quantos porcentos % você quer aumentar e diminuir do valor: "))
print('-=' * 25)
print(f'Aumentando {taxa}% de R${n} temos R${moeda.aumentar(n, taxa)}')
print(f'Diminuindo {taxa}% de R${n} temos R${moeda.diminuir(n, taxa)}')
print(f'A metade de R${n} vale R${moeda.metade(n)}')
print(f'O dobro de R${n} vale R${moeda.dobro(n)}')
