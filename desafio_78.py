lista = []
pos_maior = []
pos_menor = []
for x in range (0,5):
    n = int(input('Digite um valor:'))
    lista.append(n)


for i, k in enumerate(lista):
    if k == max(lista):
        pos_maior.append(i)
    if k == min(lista):
        pos_menor.append(i)
   

print(f'O maior valor digitado foi {max(lista)} e suas posições na lista são {pos_maior}')
print(f'O menor valor digitado foi {min(lista)} e suas posições na lista são {pos_menor}')