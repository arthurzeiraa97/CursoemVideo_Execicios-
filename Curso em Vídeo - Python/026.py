frase = str(input("Digite uma frase: ")).strip().upper()
print("A letra A aparece {} vezes na frase!".format(frase.count('A')))
print("A letra A apareceu, primeiramente, na posição {}!".format(frase.find('A')+1)) # +1 pq o codigo le a primeira posiçao como [0] e nao [1]
print(('A letra A apareceu, por último, na posição {}'.format(frase.rfind('A')+1)))

