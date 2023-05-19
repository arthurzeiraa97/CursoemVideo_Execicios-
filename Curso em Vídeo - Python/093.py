dados = dict()
gols = []
dados['Nome'] = str(input('Nome do Jogador: ')).capitalize()
n = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(n):
    gols.append(int(input(f'     Quantos gols na partida {c+1}? ')))
dados['Gols'] = gols
dados['TotGols'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-=' * 30)
print(f'O {dados["Nome"]} jogou {n} partidas: ')
for i in range(len(gols)):
    print(f'     => Na partida {i+1} marcou {gols[i]} gol(s).')
print(f'Totalizando {sum(gols)} gols!')
print('-=' * 30)
