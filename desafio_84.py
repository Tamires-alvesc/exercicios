lista = []
dado = []
ans = ' '
pessoas = 0
pesado = []
leve = []
maiores = []
menores = []

while True:
    dado.append(str(input('Digite o nome da pessoa:')))
    dado.append(float(input('Digite o peso da pessoa:')))
    lista.append(dado[:])
    dado.clear() # para não ficar acumulando dados da lista temporária na principal
    pessoas += 1
    ans = str(input('Quer continuar?[S/N]')).upper().strip()[0]

    if ans == 'N':
        break

for p in lista:
    if p[1] > 70:
        pesado.append(p[0])
        maiores.append(p[1])
    else:
        leve.append(p[0])
        menores.append(p[1])

print(f'Foram cadastradas {pessoas} pessoas no total') #ou len(lista)
print(f'As pessoas mais pesadas são {pesado}. Maior peso {max(maiores)}')
print(f'As pessoas mais leves são {leve}. Menor peso {min(menores)}')
