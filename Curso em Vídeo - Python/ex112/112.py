from utilidadesCev import func_dados, func_moeda

p = dados.leiaDindin('Insira o preço: R$ ')
taxa_aum = float(input("Quantos porcentos % você quer aumentar do valor: "))
taxa_dim = float(input("Quantos porcentos % você quer diminuir do valor: "))

moeda.resumo(p, taxa_aum, taxa_dim, "Resumo dos Valores")
