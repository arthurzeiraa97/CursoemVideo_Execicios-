pessoas = []
dados = []
i = 0
pesos = []
nomemaior = []
nomemenor = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso em Kg: ')))
    i += 1
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Voce quer continuar? [S/N]: ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Opção inválida...\nDigite somente [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
print('*-' * 30, end='')
print('*')
print(f'Você cadastrou, no total, {i} pessoas!')
for c in range(0, len(pessoas)):
    if c == 0:
        pesos.append(pessoas[c][1])
        nomemaior.append(pessoas[c][0])
        nomemenor.append(pessoas[c][0])
    else:
        if pessoas[c][1] > max(pesos):
            pesos.append(pessoas[c][1])
            nomemaior.clear()
            nomemaior.append(pessoas[c][0])
        elif pessoas[c][1] == max(pesos):
            pesos.append(pessoas[c][1])
            nomemaior.append(pessoas[c][0])
        elif pessoas[c][1] == min(pesos):
            pesos.append(pessoas[c][1])
            nomemenor.append(pessoas[c][0])
        elif pessoas[c][1] < min(pesos):
            pesos.append(pessoas[c][1])
            nomemenor.clear()
            nomemenor.append(pessoas[c][0])
print(f'O maior peso foi de {max(pesos)} Kg cadastrados nos seguintes nomes -> {nomemaior}')
print(f'Já o menor peso foi de {min(pesos)} Kg para as seguintes pessoas -> {nomemenor}')
print('*-' * 30, end='')
print('*')
