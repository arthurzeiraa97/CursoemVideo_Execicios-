import math
co = float(input('Digite um valor para o cateto oposto ='))
ca = float(input('Digite outro valor para o cateto adjascente ='))
h = math.hypot(co,ca)
print('Dados os valores de cateto oposto = {} e cateto adjascente = {}, a hipotenusa desse triângulo retângulo vale {:.2f}'.format(co,ca,h))
