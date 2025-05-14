#Listas

#lista.append - adicionar elementos

#lista.insert(0,x)

#del lista[3]

#lista.pop(3)

#lista.remove('x')

#lista.sort()

#lista.sort(reverse=True)

#valores = list(range(4,11))


valores = []
valores.append(5)
valores.append(9)
valores.append(4)

#for cont in range(0,5):
    #valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

#igualando uma lista a outra, ambas mudam definitivamente (há uma ligação entre elas)

#b = a[:] (não é feita uma ligação, apenas uma cópia de uma lista em outra)