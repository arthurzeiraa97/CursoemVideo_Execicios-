import moeda

n = float(input("Digite um valor: R$ "))
taxa = float(input("Quantos porcentos % você quer aumentar e diminuir do valor: "))
print('-=' * 30)
print(f'Aumentando {taxa}% de R${moeda.moeda(n)} temos R${moeda.moeda(moeda.aumentar(n, taxa))}')
print(f'Diminuindo {taxa}% de R${moeda.moeda(n)} temos R${moeda.moeda(moeda.diminuir(n, taxa))}')
print(f'A metade de R${moeda.moeda(n)} vale R${moeda.moeda(moeda.metade(n))}')
print(f'O dobro de R${moeda.moeda(n)} vale R${moeda.moeda(moeda.dobro(n))}')
