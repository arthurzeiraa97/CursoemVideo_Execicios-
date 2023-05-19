# listas parte 2
# pessoal = [['amanda', 13], ['roberto', 25], ['renato', 53], ['jéssica', 36]]
# print(pessoal[3][1])
""" for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos!') """
pessoal = []
dados = []
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoal.append(dados[:])
    dados.clear()
print(pessoal)
