alunos = {'Nome': str(input('Nome: ')), 'Média': float(input('Média: '))}
print(f'O {alunos["Nome"]} obteve uma média igual a {alunos["Média"]}!')
if alunos['Média'] > 7.0:
    print('Portanto, APROVADO!')
if 5 < alunos['Média'] < 7:
    print('Portanto, em EXAME!')
if alunos['Média'] <= 5:
    print('Portanto, REPROVADO(A)...')
