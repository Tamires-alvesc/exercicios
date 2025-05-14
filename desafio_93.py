aproveitamento = []

jogador = dict()

jogador['nome'] = str(input('Entre com o nome do jogador: '))

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

total = 0

for c in range(1, partidas + 1):
    gols = int(input(f'Quantidade de gols feitos na {c}ª partida? '))
    aproveitamento.append(gols)
    total += gols

jogador['gols'] = aproveitamento[:]

jogador['total'] = total

print(jogador)

print('-='*25)
for k , v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

print('-='*25)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for c in range(1, partidas + 1):  # ou for i, v in enumerate(aproveitamento) 
    print(f'Na partida {c} fez {aproveitamento[c-1]} gols.') # ou print (f'Na partida {i+1} fez {v} gols')
print(f'Foi um total de {total} gols')