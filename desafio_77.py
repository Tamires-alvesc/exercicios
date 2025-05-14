tupla = ('celular', 'teclado', 'fone', 'mouse', 'tela', 'caneta', 'grampeador', 'cabo')

k = len(tupla)
vogais = ('a', 'e', 'i', 'o', 'u')


for c in range (0,k+1):
    v = ()
    for x in range (0,5):
        if vogais[x] in tupla[c]:
            v = v + (vogais[x],)  
    print(f'As vogais da palavra {tupla[c]} são {v}')


#for palavra in tupla:
#    v = ()
#    for vogal in vogais:
#       if vogal in palavra:
#            v = v + (vogal)
#    print(f'As vogais da palavra {palavra} são {v}')