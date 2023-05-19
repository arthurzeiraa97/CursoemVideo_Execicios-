def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Idade = {idade} anos -> ', end='')
    if 18 <= idade <= 70:
        return 'VOTO OBRIGATÓRIO!'
    elif 16 <= idade < 18 or idade > 70:
        return 'VOTO OPCIONAL!'
    else:
        return "NÃO VOTA!"


print('-=' * 25)
n = int(input("Em que ano você nasceu? "))
print(voto(n))
