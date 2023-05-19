vel = float(input('Qual foi a velocidade que o seu carro passou pelo pardal em km/h?  '))
if vel > 80:
    multa = 7*(vel-80)
    print('SE FUDEU KKKK VC FOI MULTADO, POIS ESTAVA ACIMA DO LIMITE QUE É DE 80 KM/H E VAI PAGAR R${:.2f} DE MULTA!'.format(multa))
else:
    print('Sua velocidade estava abaixo do limite!')
