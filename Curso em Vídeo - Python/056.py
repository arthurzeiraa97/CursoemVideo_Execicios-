soma = 0
m = 0 # contador de mulheres
oldest = 0 # idade do mais velho
nomeoldest = '' # nome do mais velho
for c in range(1,5):
    print('------ {}ª PESSOA ------'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ').upper())
    soma = soma + idade # somatório de todas as idades

    if sexo == 'M' and c == 1:
        oldest = idade # como eu li um unico valor de idade, esse valor é o maior valor possivel
        nomeoldest = nome
    else:
        if sexo == 'M' and idade > oldest: # se o novo valor que eu ler for maior que o anterior, o novo valor de idade sera o maior(oldest)
            oldest = idade # portanto idade passa a ser(receber) o maior valor ou a idade do mais velho
            nomeoldest = nome
    if sexo == 'F' and idade < 20:
        m = m + 1
media = soma / 4

print('O homem mais velho tem {} anos e se chama {}!!'.format(oldest, nomeoldest))
print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('E nesse grupo temos {} mulheres com menos de 20 anos!'.format(m))


#total_idade = 0
#listanh = []
#listaih = []
#m20 = 0
#for c in range(1, 5):
#    print(f"------ {c}° PESSOA -------")
#    nome = str(input("Qual é seu nome? ")).strip().title()
#    idade = int(input("Idade: "))
#    total_idade += idade
#    Sexo = int(input("""Digite [1] para sexo masculino e
#Digite [2] para sexo feminino:"""))
 #   if Sexo == 1:
 #       listanh.append(nome)
 #       listaih.append(idade)
 #   if Sexo == 2 and idade < 20:
 #       m20 += 1
#print(f"A idade média do grupo é {total_idade / 4:.2f} anos")
#print(f"O homem mais velho tem {max(listaih)} anos e seu nome é {listanh[listaih.index(max(listaih))]}")
#print(f'E no total {m20} mulheres tem menos de 20 anos. ')

