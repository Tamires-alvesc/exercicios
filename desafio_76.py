tupla = ('Banana', '2.00', 'Uva', '3.00', 'Pão', '5.00')

print('PRODUTO-------PREÇO')
print(f'{tupla[0]}......R$ {tupla[1]}')
print(f'{tupla[2]}.........R$ {tupla[3]}')
print(f'{tupla[4]}.........R$ {tupla[5]}')


print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":.^40}')

for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end = '')
    else:
        print(f'R${tupla[pos]:.>7}')
print('-'*40)