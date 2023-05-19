br = ('corinthias','palmeiras', 'santos', 'grêmio', 'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
      'atlético mg','botafogo', 'atlético pr', 'bahia', 'sâo paulo', 'fluminense', 'sport', 'vitória', 'coritiba',
      'avaí', 'ponte preta', 'atlético go')
print('===' * 30)
print('Classificação do Brasileirão 2017: ')
for i, time in enumerate(br):
      print(f'{i+1}º {time}')
print('===' * 30)
print(f'Os 5 primeiros colocados são {br[0:5]}')
print('===' * 30)
print(f'Os 4 times rebaixados são {br[16:]}')
print('===' * 30)
print(f'Times em ordem alfabética: {sorted(br)}')
print('===' * 30)
print(f'A {br[7]} está na 8ª posição.')
