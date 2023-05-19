c = str(input('Informe a expressão: '))
parenteses = []
for i in c:
    if i == '(':
        parenteses.append(i)
    elif i == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(i)
            break
if len(parenteses) == 0:
    print('A sua expressão está correta!')
else:
    print('A sua expressão está inválida!')
