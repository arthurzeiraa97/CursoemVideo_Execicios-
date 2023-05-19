n = int(input('Digite o seu ano de nascimento: '))
idade = 2023 - n
if idade == 18:
    print('Você completa 18 anos esse ano! '
          'Você deve ser alistar imediatamente!')
elif idade < 18:
    print('Esse ano você completa {} anos, portanto ainda faltam {} anos para você se alistar!'.format(idade,18-idade))
else:
    print('Você tem {} anos! Seu alistamento foi em {}!'.format(idade,n+18))