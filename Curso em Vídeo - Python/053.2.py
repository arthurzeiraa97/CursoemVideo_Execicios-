frase = str(input('Digite uma frase: ')).upper()
junto = ''.join(frase.split())
for letra in range(len(junto) - 1, -1, -1):
    print(junto[letra], end='')
