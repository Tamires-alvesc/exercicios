from random import randint

lista = []
num = int(input('Quantos jogos serão gerados?\n'))


for n in range(0, num):
    jogo = []
    while len(jogo) < 6:
        new_n = randint(1,60)
        if new_n not in jogo:
            jogo.append(new_n)
            jogo.sort()
    if jogo not in lista:
        lista.append(jogo[:])
print('Os jogos gerados foram:\n')

for n in range(0, num):
    print(f'Jogo {n + 1}: {lista[n]}')

#for i, l in enumerate(lista):
#   print(f'Jogo {i}: {l}')