import time
import random

print('SUAS OPÇÕES:')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
x = int(input('Qual é a sua jogada? '))
pc = random.randint(1,3)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=' * 19)

if pc == 1 and x == 1:
    print('Computador jogou PEDRA\nJogador jogou PEDRA\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nEMPATE!')
elif pc == 1 and x == 2:
    print('Computador jogou PEDRA\nJogador jogou PAPEL\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nJOGADOR VENCE!')
elif pc == 1 and x == 3:
    print('Computador jogou PEDRA\nJogador jogou TESOURA\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nCOMPUTADOR VENCE!')
elif pc == 2 and x == 1:
    print('Computador jogou PAPEL\nJogador jogou PEDRA\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nCOMPUTADOR VENCE! ')
elif pc == 2 and x == 2:
    print('Computador jogou PAPEL\nJogador jogou PAPEL\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nEMPATE!')
elif pc == 2 and x == 3:
    print('Computador jogou PAPEL\nJogador jogou TESOURA\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nJOGADOR VENCE!')
elif pc == 3 and x == 1:
    print('Computador jogou TESOURA\nJogador jogou PEDRA\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nJOGADOR VENCE!')
elif pc == 3 and x == 2:
    print('Computador jogou TESOURA\nJogador jogou PAPEL\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nCOMPUTADOR VENCE!')
elif pc == 3 and x == 3:
    print('Computador jogou TESOURA\nJogador jogou TESOURA\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nEMPATE!')