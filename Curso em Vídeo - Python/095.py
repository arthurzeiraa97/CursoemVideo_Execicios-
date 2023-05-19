from time import sleep
dados = {}
time = []
gols = []
print(f'{"<< FutStats 2023 >>":=^60}')

while True:
    gols.clear()
    dados['Nome'] = str(input('Nome do Jogador: ')).capitalize()
    n = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for c in range(n):
        gols.append(int(input(f'     Quantos gols na partida {c+1}? ')))
    dados['Gols'] = gols[:]
    dados['TotGols'] = sum(gols)
    time.append(dados.copy())
    dados.clear()
    opcao = str(input("Você quer continuar? [S/N] ")).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('ERRO!\nDigite somente S ou N: ')).upper().strip()[0]
    if opcao == 'N':
        break

print('-' * 60)
print(f'{"Cód.":<3}', f'{"Nome":>5}', f'{"Gols":>10}', f'{"Total de Gols":>25}')
print('-' * 60)
for i, v in enumerate(time):
    print(f'{i:>5}', f'{v["Nome"]:<10}', f'{str(v["Gols"]):<20}', f'  {v["TotGols"]:<25}')
print('-' * 60)

while True:
    n = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if n == 999:
        break
    while n > len(time)-1:
        n = int(input(f'ERRO! Não existe jogador {n} na lista!\nDigite um código válido: '))
    print(f'Levantamento do jogador -> {time[n]["Nome"]}')
    for v, c in enumerate(time[n]["Gols"]):
        print(f'     No jogo {v+1} fez {c} gols.')
    print('-=' * 30)

print("Finalizando", end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
print(f'{"<< FutStats 2023 >>":=^60}')
