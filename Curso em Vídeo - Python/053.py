frase = str(input('Digite uma frase: ')).upper().split()
frase = ''.join(frase)
inverter = frase[::-1]
print('O inverso de {} é {}'.format(frase,inverter))
if frase == inverter:
    print("A frase digitada é um palíndromo!")
else:
    print('A frase digitada nao é um palíndromo!')
