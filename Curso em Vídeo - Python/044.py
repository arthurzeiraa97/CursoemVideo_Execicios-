print('======== LOJAS PORTO ========')
p = float(input('Preço das compras R$ '))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
x = int(input('Qual é a opção? '))
if x == 1:
    print('Sua compra de R$ {:.2f} receberá um desconto de 10% passando a custar R$ {:.2f}!'.format(p, 0.9*p))
elif x == 2:
    print('Ao pagar à vista no cartão, sua compra que inicialmente custava R$ {:.2f} com 5% de desconto passará a '
          'custar'
          'R$ {:.2f}! '.format(p, 0.95*p))
elif x == 3:
    print('Você pagará 2 parcelas de R$ {:.2f} com o preço final de R$ {:.2f}!'.format(p/2, p))
elif x == 4:
    n = int(input('Número de parcelas: '))
    pf = 1.2 * p
    print('Sua compra de R$ {:.2f} será parcelada em {}x de R$ {:.2f} COM JUROS, custará no final R$ {:.2f}!'.format(p, n, pf/n, pf))
else:
    print('Opção inválida de pagamento! Tente novamente!')

