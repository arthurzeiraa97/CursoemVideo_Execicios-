# tuplas
#tuplas sao imutaveis
#posso add strings e numeros numa mesma tupla. exe: pessoa = ('ana', 22, 'M, 78.89)

#lanche = 'suco', 'pizza', 'pudim', 'salada' # tuplas podem ser escritas dentro dos () ou fora
#lanche = ('suco', 'pizza', 'pudim')
#lanche[2] = 'alface' # esse comando mostra que nao se pode atribuir novos elementos à uma tupla
#print(lanche)
#print(sorted(lanche))

'''for comida in lanche:
    # print(f'{comida}', end=' ') ou..
    print(f'eu vou comer {comida}')'''

'''for i in range(0,len(lanche)): #maneira diferente de contar os itens da tupla
    print(i)'''

'''for i in range(0,len(lanche)): #maneira diferente de printar os itens da tupla
    print(lanche[i])'''

'''for pos, comida in enumerate(lanche): # enumerate nos da o item e a posiçao
    print(f'O lanche {comida} está na posiçao {pos}')'''

a = (1, 2, 3, 5, 8)
b = (4, 5, 6, 7)
c = a + b #concatenaçao de itens das duas tuplas
print(c)
print(c.count(5)) # conta quantas vezes o num 5 aparece na tupla c
print(c.index(8)) # mostra a posiçao que o item está
