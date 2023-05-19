n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua média foi {}! ABAIXO de 5.0, portanto você está REPROVADO!'.format(media))
elif 5.0 <= media <= 6.9:
    print('Sua média foi {}! Ficou entre 5.0 e 6.9, portanto você está de EXAME!'.format(media))
else:
    print('Sua média foi {}! Maior que 6.9, portanto VOCÊ FOI APROVADO!'.format(media))
