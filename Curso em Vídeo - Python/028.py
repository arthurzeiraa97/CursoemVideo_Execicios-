import random
import time
print('Vou pensar em um número entre 0 e 5. Tente Advinhar...')
time.sleep(2)
num = random.randint(0,5)
x = float(input('Em que número eu pensei?: '))
print('PROCESSANDO...')
time.sleep(1.5)
if x == num:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Eu pensei no {}!'.format(num))
