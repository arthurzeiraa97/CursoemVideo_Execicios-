#  ERROS E EXCEÇOES

try:
    a = int(input('Informe um número: '))
    b = int(input('Informe outro número: '))
    r = a/b
except TypeError:
    print(f'Tivemos um problema com os dados que voce digitou!')
except Exception as erro:
    print(f'Tivemos um erro do tipo {erro}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre!')

