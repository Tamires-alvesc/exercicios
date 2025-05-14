from random import randint


def sorteia(lista):
    for c in range(1,6):
        n = randint(1,100)
        lista.append(n)
    print(f'Os números sorteados foram {lista}')


def somaPar(lista):
    c = 0
    for valor in lista:
        if valor % 2 == 0:
            c += valor
    print(f'A soma dos valores pares sorteados é {c}')




numeros = []
sorteia(numeros)
somaPar(numeros)




