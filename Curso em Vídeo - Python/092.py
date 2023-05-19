dados = {'Nome': str(input('Nome: ').capitalize().strip()),
         'Idade': 2023 - int(input('Ano de nascimento: ')),
         'Carteira de trabalho': int(input('Carteira de trabalho [0 não tem]: ')),
         }
if dados['Carteira de trabalho'] == 0:
    print('-=' * 30)
    for k, v in dados.items():
        print(f'-> {k}: {v}')
    print('-=' * 30)
else:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    print('-=' * 30)
    for k, v in dados.items():
        print(f'-> {k}: {v}')
    if 2023-dados['Ano de contratação'] >= 30 and dados['Idade'] >= 60:
        print(f'-> Idade de aposentadoria: Já pode se aposentar!')
    else:
        print(f'-> Idade de aposentadoria: {dados["Idade"] + ((dados["Ano de contratação"] + 30) - 2023)}')
    print('-=' * 30)
