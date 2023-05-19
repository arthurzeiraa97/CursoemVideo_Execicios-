from random import randint
from time import sleep
from operator import itemgetter

dados = {'Jogador_1': randint(1, 6),
         'Jogador_2': randint(1, 6),
         'Jogador_3': randint(1, 6),
         'Jogador_4': randint(1, 6)
         }
ranking = []
sleep(1)
print('-=' * 15)
print(f'{" Valores Sorteados foram: ":^30}')
sleep(1)
for k, v in dados.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print(f'{"Ranking final:":^30}')
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}')
print('-=' * 15)
