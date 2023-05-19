lista = []
dados = {}
soma = 0

while True:
    dados['Nome'] = str(input('Nome: ')).capitalize()
    dados['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = str(input('ERRO!\nDigite somente M ou F: ')).upper().strip()[0]
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    lista.append(dados.copy())
    opcao = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('ERRO!\nDigite somente S ou N: ')).upper().strip()[0]
    if opcao == "N":
        break

print('-=' * 30)
print(f'A) Ao todo, {len(lista)} pessoas foram cadastradas.')

media = soma / len(lista)
print(f'B) A média de idade é de {media:.1f} anos. ')

print('C) As mulheres cadastradas foram:', end=' ')
for c in lista:
    if c['Sexo'] in 'F':
        print(f'[{c["Nome"]}]', end=' ')

print('\nD) Lista das pessoas que estão acima da média de idade:')
for c in lista:
    if c['Idade'] > media:
        print(f'    Nome = {c["Nome"]}; Sexo = {c["Sexo"]} e Idade = {c["Idade"]} anos.')
print(f'{" << Cadastro Finalizado >> ":=^60}')
