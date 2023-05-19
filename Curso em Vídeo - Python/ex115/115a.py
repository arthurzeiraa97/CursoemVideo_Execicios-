import funcs
from time import sleep


while True:
    sleep(1)
    resp = funcs.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1 or resp == 2:
        sleep(1)
        funcs.titulo(f' Opção {resp} ')
    elif resp > 3:
        print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
    elif resp == 3:
        sleep(1)
        print('Saindo do sistema...')
        break
"""while n != 3:
    try:
        n = int(input('\033[1;33mSua opção: \033[m'))
    except (ValueError, TypeError):
        print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
    except KeyboardInterrupt:
        print('\n\033[1;31mEntrada de dados interrompida!\033[0m')
        break
    else:
        if 1 <= n <= 2:
            sleep(1)
            funcs.titulo(f' Opção {n} ')
            break
        elif n > 3:
            print('\033[1;31mErro! Digite um número inteiro válido.\033[m')"""

sleep(0.5)
funcs.titulo(' Até logo! ')
