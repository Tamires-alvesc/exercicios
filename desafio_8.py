r = 1
while r != 0:
    r = float(input('Quantos reais você tem para troca? \nR$'))
    dol = round(r/(5.91),2)

    print(f'Você pode comprar {dol} dólares com {r} reais\n')
#print('Você pode comprar {:.2f} dólares com {} reais'.format(dol,r))