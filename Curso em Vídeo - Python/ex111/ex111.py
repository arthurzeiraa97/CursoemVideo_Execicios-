from utilidadesCev import moeda

print('-=' * 30)
n = float(input("Digite um valor: R$ "))
taxa_aum = float(input("Quantos porcentos % você quer aumentar do valor: "))
taxa_dim = float(input("Quantos porcentos % você quer diminuir do valor: "))

moeda.resumo(n, taxa_aum, taxa_dim, "RESUMO DOS VALORES")
