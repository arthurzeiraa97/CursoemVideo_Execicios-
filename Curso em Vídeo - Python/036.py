casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite quanto voce ganha: R$ '))
anos = float(input('Digite em quantos anos voce quer pagar: '))
meses = anos*12
prestacao = casa/meses
if prestacao <= 0.3*salario:
    print('Parabens! Seu empréstimo foi APROVADO! A parcela será de {:.2f} por mês durante os proximos {} anos!'.format(prestacao,anos))
else:
    print('Infelizmente seu empréstimo foi NEGADO! A prestação será de R${:.2f} e seu salário de R${} é muito baixo!'.format(prestacao,salario))
