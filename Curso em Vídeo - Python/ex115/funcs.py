def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Entrada inválida.\033[0m')
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de dados interrompida!\033[0m')
            return 0
        else:
            return n


def titulo(txt):
    print(f'\033[1;38m{txt:=^40}\033[m')


def menu(lista):
    from time import sleep
    titulo('<< SISTEMA PRINCIPAL >>')
    c = 1
    for item in lista:
        print(f'\033[1;32m{c}\033[m - \033[1;36m{item}\033[m')
        c += 1
    print('\033[1;38m==\033[m' * 20)
    sleep(1)
    opc = leiaInt('\033[1;33mSua opção: \033[m')
    return opc


def leiaArq(lista):
    try:
        a = open(lista, 'rt')
    except Exception as error:
        print(f'erro {error} ao ler o arquivo!')
    else:
        for line in a:
            item = line.split(';')
            item[1] = item[1].replace('\n', '')
            print(f'{item[0]:<30}{item[1]:>5} anos')


def adicionarArq(nome, txt='nao informado', n=0):
    try:
        a = open(nome, 'at')
    except Exception as error:
        print(f'Erro {error} ao abrir o arquivo!')
    else:
        try:
            a.write(f'{txt};{n}\n')
        except:
            print('Erro ao adicionar cadastro no arquivo!')
        else:
            print(f'{txt} adicionado(a) com sucesso!')


def arqExiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'w')
        a.close()
    except Exception:
        print('Erro ao criar o arquivo!')
    else:
        print(f'{nome} criado com sucesso!')
