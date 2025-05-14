lista = []

for k in range(0,5):
    peso = float(input(f'Entre com o peso da {k}ª pessoa em kg:'))
    lista.append(peso)

print(f'O maior peso lido é {max(lista)} e o menor é {min(lista)}')


#maior = 0 
#menor = 0
#for p in range(1,6)
#   peso = float(input(f'Peso da {p}ª pessoa:'))
#   if p == 1:
#       maior = peso 
#       menor = peso
#   else:
#       if peso > maior:
#            maior = peso
#       if peso < menor:
#            menor = peso
#print(f'O maior peso lido foi de {maior} Kg')
#print(f'O menor peso lido foi de {menor} Kg')