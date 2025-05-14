from time import sleep


def maior(*núm):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in núm:
        print(valor, end = ' ', flush = True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior entre os valores informados é {maior}')


maior(1, 3, 6, 0, -2)

maior(2, 9)