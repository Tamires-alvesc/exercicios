#colocar um dicionário em ordem (jogador que tirou numero mais alto no dado vence)

from random import randint
jogo = dict()
final = list()

for c in range(1,5):
    jogo['jogador'] = c
    jogo['resultado'] = randint(1,6)
    final.append(jogo.copy())
print(final)

resultado_ordenado = []

for e in final:
    jogador = e['jogador']
    valor = e['resultado']
    if len(resultado_ordenado) == 0:
        resultado_ordenado.append(e)
    else:
        n_items =  len(resultado_ordenado)
        for i in range(0, n_items):
            j = resultado_ordenado[i]
            if valor > j['resultado']:
                resultado_ordenado.insert(i, e)
                break
        else:
            resultado_ordenado.append(e)
    print(f'O jogador {jogador} tirou {valor}')


for r in resultado_ordenado:
    print(f'O jogador {r['jogador']} tirou o {r['resultado']}')


