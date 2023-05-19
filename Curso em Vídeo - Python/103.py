def ficha(nome="<desconhecido>", n="0"):
    print(f'O jogador {nome} fez {n} gol(s) no campeonato!')


txt = str(input("Informe o nome do jogador: ")).capitalize()
num = str(input("Agora, informe o número de gols marcados: "))
if num.isnumeric():
    num = int(num)
else:
    num = '0'
if txt.strip() == '':
    ficha(n=num)
else:
    ficha(txt, num)
