from random import randint
from time import sleep

n1 = randint(0,5)

n2 = int(input('Adivinhe qual número inteiro entre 0 e 5 o computador escolheu:\n'))

print('Processando....')
sleep(2)

if n2 == n1:
    print(f'Acertou. O computador escolheu o número {n1}')
else:
    print(f'Errou. O computador escolheu o número {n1}')
