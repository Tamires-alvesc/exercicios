def ficha(nome = ' ', gols = 0):
    print(f'Ficha do jogador:')
    print(f'NOME:.......................GOLS:')
    if nome == ' ' and gols != 0:
        print(f'<desconhecido>........................{gols}')
    if nome != ' ' and gols == 0:
        print(f'{nome}........................<não informado>')
    if nome == ' ' and gols == 0:
         print(f'<desconhecido>..................<não informado>')
    else:
        print(f'{nome}........................{gols}')


ficha('José', 3)
ficha('Talisson', 8)
ficha(' ',)
ficha(' ', 5)