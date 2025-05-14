from random import randint

n = randint(0,10) 
k = 0
cont = 0
while k != n:
    if k == 0:
        k = int(input('Escreva o seu palpite do número que o PC escolheu:'))
        print('Você perdeu. Tente novamente...')
    else:
        k = int(input('Escreva o seu palpite do número que o PC escolheu:'))
        print('Você perdeu. Tente novamente...')
    cont += 1
print(f'Você e o PC escolheram o mesmo número na {cont}ª tentativa e o número foi {n}!')