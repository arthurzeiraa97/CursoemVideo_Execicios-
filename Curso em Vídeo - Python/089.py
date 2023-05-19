print('-=' * 30)
alunos = []
boletim = []
media = 0
while True:
    alunos.append(str(input('Nome: ')).capitalize())
    alunos.append(float(input('Primeira nota: ')))
    alunos.append(float(input('Segunda nota: ')))
    boletim.append(alunos[:])
    alunos.clear()
    opcao = str(input('Você quer continuar: [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Entrada inválida...\nDigite somente [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
print('-=' * 30)
print(f'{"N°"}    {"NOME":<10}{"MÉDIA":>4}')
print('-' * 60)
for c in range(len(boletim)):
    media = (boletim[c][1]+boletim[c][2])/2
    print(f'{c}     {boletim[c][0]:<10}{media:>4.2f}')
print('-' * 60)
while True:
    i = int(input('Notas detalhadas de qual aluno? [999 para sair] '))
    if i == 999:
        break
    print(f'As notas de {boletim[i][0]} são -> [{boletim[i][1]}, {boletim[i][2]}]')
    print('-' * 60)
print('Finalizando...')
print('<<< VOLTE SEMPRE! >>>')
