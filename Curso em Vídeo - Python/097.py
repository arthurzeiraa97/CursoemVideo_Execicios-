def escreva(txt):
    len(txt)
    print("=" * (len(txt) + 4))
    print(f'  {txt}')
    print("=" * (len(txt) + 4))


while True:
    escreva(str(input("Escreva o texto que você quer mostrar: ")))
    opcao = str(input('Você quer escrever mais alguma coisa? [S/N] ')).upper().strip()[0]
    while opcao not in "SN":
        opcao = str(input('ERRO!Digite somente S ou N: ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'{"<< FIM >>":=^50}')
