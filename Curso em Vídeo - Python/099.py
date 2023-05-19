from time import sleep


def maior(*num):
    print('-=' * 25)
    print("Analisando os valores informados:")
    sleep(0.75)
    print(f'Foram informados esses {len(num)} valores -> ', end='')
    sleep(0.75)
    for n in num:
        print(n, end=' ')
        sleep(0.5)
    sleep(0.75)
    print(f'\nSendo {max(num)} o maior deles.')


print(f'{"<< BEM-VINDO >>":=^50}')
sleep(0.5)
maior(3, 4, 12, 7)
sleep(0.5)
maior(33, 1, 0, 5, 23)
sleep(0.5)
maior(7, 2)
sleep(0.5)
maior(0)
sleep(0.5)
print(f'{"<< FIM >>":=^50}')
