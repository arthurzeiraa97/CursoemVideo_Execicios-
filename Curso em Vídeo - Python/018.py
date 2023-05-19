'''import math
teta = float(input('Digite o valor de um angulo em graus:'))
alfa = math.radians(teta)
s = math.sin(alfa)
c = math.cos(alfa)
t = math.tan(alfa)
print('O ângulo {} graus tem como cosseno = {:.3f}, seno = {:.3f} e tangente = {:.3f} '.format(teta,s,c,t))'''

''' de outra maneira'''
''' math.radians transforma o angulo de entrada de graus para radianos'''
import math

teta = float(input('Digite um ângulo em graus:'))
sen = math.sin(math.radians(teta))
cos = math.cos(math.radians(teta))
tan = math.tan(math.radians(teta))
print('O ãngulo {} graus tem seno = {:.2f} \nCos = {:.2f} \nTangente = {:.2f}'.format(teta,sen,cos,tan))
