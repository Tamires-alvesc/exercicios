aproveitamento = []
equipe = []
jogador = dict()
ans = ' '

while True:
    jogador.clear()
    jogador['nome'] = str(input('Entre com o nome do jogador: '))

    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? ')) #o numero de partidas é a quantidade de elementos da lista gols
    total = 0
    aproveitamento.clear()
    for c in range(1, partidas + 1):
        gols = int(input(f'Quantidade de gols feitos na {c}ª partida? '))
        aproveitamento.append(gols)
        total += gols

    jogador['gols'] = aproveitamento[:]
    jogador['total'] = total
    equipe.append(jogador.copy())

    while True:
        ans = str(input('Você quer continuar cadastrando jogadores?[S/N]')).upper().strip()[0]
        if ans in 'SN':
            break
        else:
            print('Digite apenas S ou N')
    if ans == 'N':
        break
    
print('-='*30)
print('cod', end= '')
for i in jogador.keys():
    print(f'{i:<15}', end= '')
print()
print('-'*40)
for k, v in enumerate(equipe):
    print(f'{k:>4}', end= '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(equipe):
        print(f'Erro! Não existe jogador com código {busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {equipe[busca]["nome"]}:')
        for i, g in enumerate(equipe[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
                


   
