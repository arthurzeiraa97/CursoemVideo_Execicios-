print('-=-' * 20)
print('            Bem vindo à seção de cadastramento!')
print('-=-' * 20)
i = s = w = 0
while True:
    idade = int(input('Informe a idade da pessoa: '))
    sexo = str(input('Informe o sexo da pessoa [M/F]: ')).upper().strip()[0]
    print('-=-' * 20)
    while sexo not in 'MF':
        sexo = str(input('Dadi incorreto...Informe somente M ou F para o sexo da pessoa: ')).upper().strip()[0]
        print('-=-' * 20)
    if idade > 18:
        i += 1
    if sexo == 'M':
        s += 1
    if sexo == 'F' and idade < 20:
        w += 1
    n = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while n not in 'SN':
        n = str(input('Digitação incorreta... Você quer continuar? [S/N] ')).upper().strip()[0]
        print('-=-' * 20)
    if n == 'N':
        break
print('-=-'*20)
print('                      Fim de cadastro!')
print('-=-' * 20)
print('As informações coletadas foram as seguintes:')
print(f'{i} pessoas tem mais que 18 anos.\n{s} homens foram cadastrados\ne {w} mulheres tem menos de 20 anos!')
