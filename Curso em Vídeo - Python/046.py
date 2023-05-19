import time
import emoji

festa = str(input('Qual a comemoração? ')).upper()

for c in range(10,0,-1):
    print(c)
    time.sleep(1)
print(emoji.emojize('FELIZ {}! :fireworks::sparkler:'.format(festa)))

