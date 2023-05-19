i = soma = n = 0
while True:
    n = int(input('Digite um número [999 para sair do programa]: '))
    if n == 999:
        break
    i += 1
    soma += n
print(f'Você digitou {i} números e soma entre eles foi {soma}!')
