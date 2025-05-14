from random import randint

tupla = (0,)
for k in range (0, 5):  
    n = randint(0,100)
    tupla = tupla + (n,)
print(f'Os valores sorteados foram{tupla}')

print (f'O maior valor na tupla é {max(tupla)} e o menor valor na tupla é {min(tupla)}')