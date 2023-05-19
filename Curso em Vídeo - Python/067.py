# tabuada v3.0
while True:
    x = int(input('Você quer ver a tabuada de qual valor? '))
    if x < 0:
        break
    print('=='*20)
    for c in range(1,11):
        print(f'{x} x {c} = {x*c}')
    print('=='*20)
print('Tabuada encerrada! Volte Sempre!')
