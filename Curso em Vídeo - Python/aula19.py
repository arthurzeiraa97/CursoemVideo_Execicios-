#  dicionários!
"""pessoas = {'Nome': 'Amanda', 'Idade': '23', 'Sexo': 'F'}
pessoas['peso'] = 72.3
for k, v in pessoas.items():
    print(f'{k} = {v}')"""

"""brasil = []
estado_1 = {'UF': 'Santa Catarina', 'Sigla': 'SC'}
estado_2 = {'UF': 'Paraná', 'Sigla': 'PR'}
brasil.append(estado_1)
brasil.append(estado_2)
print(brasil)
print(brasil[1]['UF'])
print(brasil[0]['Sigla'])"""

estados = dict()
brasil = list()
for i in range(3):
    estados['UF'] = str(input('Nome do estado: '))
    estados['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estados.copy())  # NAO ESQUECER DISSO!
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')

