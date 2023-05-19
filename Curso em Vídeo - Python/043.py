peso = float(input('Digite o seu peso em kg: '))
alt = float(input('Digite a sua altura em metros: '))
imc = peso / (alt * alt)
if imc < 18.5:
    print('Seu IMC vale {:.2f}: Abaixo do peso!'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC vale {:.2f}: Peso ideal!'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC vale {:.2f}: Sobrepeso!'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC vale {:.2f}: Obesidade!'.format(imc))
else:
    print('Seu IMC vale {:.2f}: Obesidade mórbida'.format(imc))

