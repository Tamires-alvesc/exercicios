#15 primeiros colocados no Brasileirao
pos = ('Atlético', 'Bahia', 'Botafogo', 'Ceará', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Mirassol', 'Palmeiras', 'Red Bull Bragantino')

pos5 = pos[0:5]

print(f'Os 5 primeiros colocados são {pos5}')

pos4 = pos[-4:]

print(f'Os 4 últimos colocados são {pos4}')

print(f'Os times em ordem alfabética são {sorted(pos)}')

print(f'O flamengo está na posição {int(pos.index('Flamengo')) + 1}')