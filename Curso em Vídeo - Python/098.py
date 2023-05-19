from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    if i < f:
        c = i
        while c <= f:
            print(c, end=' => ')
            c += p
            sleep(0.75)
        print("FIM")
    else:
        c = i
        while c >= f:
            print(c, end=' => ')
            c -= p
            sleep(0.75)
        print("FIM")


contador(1, 10, 1)
sleep(0.75)
contador(10, 0, 2)
print(f'{"<< Agora é a sua vez de escolher a contagem! >>":=^60}')
sleep(0.75)
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))
