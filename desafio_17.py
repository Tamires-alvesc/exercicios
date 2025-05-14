import random
import math

n1 = str(input('Nome 1:'))
n2 = str(input('Nome 2:'))
n3 = str(input('Nome 3:'))
n4 = str(input('Nome 4:'))

names = [n1,n2,n3,n4]

chosen = random.choice(names)

print(f'O escolhido é {chosen}')


#ordenar

ordenado = random.shuffle(names)


print(f'A ordem de apresentação é {names}')

print(names)