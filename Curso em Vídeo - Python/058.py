import random
from time import sleep
i = 1
n = random.randint(1,10)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue advinhar qual foi?')
x = int(input('Qual o seu palpite? '))
sleep(1)
print('hmm...')
sleep(1)
while x != n:
    sleep(1)
    if x > n:
        x = int(input('Menos... Tente novamente!\nQual o seu palpite? '))
        i += 1
    if x < n:
        x = int(input('Mais... Tente Novamente!\nQual o seu palpite? '))
        i += 1
print('Parabéns! Você acertou com {} tentativas!'.format(i))
