def area(a, b):
    c = a * b
    print(f'A área de um terreno de {a} m por {b} m é de {c:.2f} m2.')


print(f'{"<< ÁREA DE TERRENO >>":=^60}')
area(float(input('Informe a largura em metros: ')), float(input('Informe o comprimento em metros: ')))
