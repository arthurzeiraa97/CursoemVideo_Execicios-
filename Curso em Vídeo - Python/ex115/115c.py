from funcs import *
from time import sleep

arquivo = 'arquivo.txt'
if not arqExiste(arquivo):
    criarArq(arquivo)


while True:
    sleep(1)
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        sleep(1)
        titulo(f' PESSOAS CADASTRADAS ')
        sleep(1)
        leiaArq(arquivo)
    elif resp == 2:
        sleep(1)
        titulo(f' CADASTRO DE NOVA PESSOA ')
        sleep(1)
        nome = str(input('Nome: ')).capitalize()
        idade = leiaInt('Idade: ')
        adicionarArq(arquivo, nome, idade)
    elif resp > 3:
        print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
    elif resp == 3:
        sleep(1)
        print('Saindo do sistema...')
        break
sleep(0.5)
titulo(' Até logo! ')
