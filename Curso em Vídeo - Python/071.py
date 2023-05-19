print('==='*13)
print('{:^39}'.format('ATM WITHDRAWS'))
print('==='*13)
n50 = n20 = n10 = n5 = n1 = 0
saque = int(input('Quanto você quer sacar? R$ '))
while True:
    if saque >= 50:
        saque = saque - 50
        n50 = n50 + 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        elif saque >= 10:
            saque -= 10
            n10 += 1
        elif saque >= 5:
            saque -= 5
            n5 += 1
        elif saque >= 1:
            saque -= 1
            n1 += 1
    if saque == 0:
        break
print(f'Serão {n50} cédulas de R$50\n{n20} cédulas de R$20\n{n10} cédulas de R$10\n{n5} cédulas de R$5\ne {n1} cédulas de R$1. ')
print('Obrigado por utilizar este terminal. Volte sempre!')

#while True:
    #    x = int(input('Qual valor você quer sacar? R$ '))
    #if x // 50 > 0:
    #   print(f'Total de {x // 50} cédulas de R$50')
    #y = x % 50
    #if y // 20 > 0:
    #   print(f'Total de {y // 20} cédulas de R$20')
    #z = y % 20
    #if z // 10:
    #    print(f'Total de {z // 10} cédulas de R$10')
    #w = z % 10
    #if w // 1 > 0:
#    print(f'Total de {w // 1} cédulas de R$1')
    #        print('===' * 13)
    #n = str(input('Quer realizar outra transação? [S/N] ')).upper().strip()[0]
    #print('===' * 13)
    #while n not in 'SN':
    #    n = str(input('Digitação incorreta!\nVocê quer realizar outra transação? [S/N]')).upper().strip()[0]
    #if n == 'N':
#    break
#print('Obrigado por utilizar este terminal. Volte sempre!')
