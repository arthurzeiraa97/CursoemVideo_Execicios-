x = float(input('Qual o valor do seu salário? R$'))
if x > 1250:
    aumento = x*1.1
    print('Você vai receber um aumento de 10%, passando a receber agora R${:.2f}!'.format(aumento))
else:
    aumento = x*1.15
    print('Você vai receber um aumento de 15%, passando a receber agora R${:.2f}!'.format(aumento))
