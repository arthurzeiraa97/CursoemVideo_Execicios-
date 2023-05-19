import urllib.request

try:
    site = urllib.request.urlopen('https://www.inter.it/it')
except Exception as erro:
    print('Site não está acessível no momento.', erro)
else:
    print("Consegui abrir o site com sucesso!")
