import moeda

print('-=' * 30)
n = float(input("Digite um valor: R$ "))
taxa_aum = float(input("Quantos porcentos % você quer aumentar do valor: "))
taxa_dim = float(input("Quantos porcentos % você quer diminuir do valor: "))

print(f'Aumentando {taxa_aum}% de {moeda.moeda(n)} temos {moeda.aumentar(n, taxa_aum)}')
print(f'Diminuindo {taxa_dim}% de {moeda.moeda(n)} temos R${moeda.diminuir(n, taxa_dim, True)}')
print(f'A metade de {moeda.moeda(n)} vale {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} vale {moeda.dobro(n, True)}')
