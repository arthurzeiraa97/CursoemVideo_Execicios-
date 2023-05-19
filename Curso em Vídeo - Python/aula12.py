nome = str(input('Qual o seu nome? '))
if nome == "Arthur":
    print('Que nome bonito!')
elif nome == 'natan' or nome == 'norton' or nome == 'riana':
    print('Eu tenho um primo com esse nome!')
else :
    print('Esse é um nome bem comum!')
print('Tenha um Bom dia, {}!'.format(nome))
