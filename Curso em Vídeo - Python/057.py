n = str(input('Informe o seu sexo [M/F]: ')).upper().strip()
while n != 'M' and n != 'F':
#while n not in 'MF': # verificando se a letra M ou F esta no input 'n'
    n = str(input('Dado inválido! Digite o seu sexo [M/F]: ')).upper().strip()
print('Sexo {} registrado com sucesso!'.format(n))
