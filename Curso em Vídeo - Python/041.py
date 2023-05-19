nasc = int(input('Ano de nascimento do atleta: '))
idade = 2023 - nasc
if idade <= 9:
    print('O atleta nasceu em {}, tem {} anos, portanto categoria MIRIM'.format(nasc,idade))
elif 9 < idade <= 14:
    print('O atleta nasceu em {}, tem {} anos, portanto categoria INFANTIL'.format(nasc,idade))
elif 14 < idade <= 19:
    print('O atleta nasceu em {}, tem {} anos, portanto categoria JÚNIOR'.format(nasc, idade))
elif 19 < idade <= 25:
    print('O atleta nasceu em {}, tem {} anos, portanto categoria SÊNIOR'.format(nasc, idade))
else:
    print('O atleta nasceu em {}, tem {} anos, portanto categoria MASTER'.format(nasc, idade))

