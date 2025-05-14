lista =[[],[]]
for k in range(1,8):
   valor = (int(input(f'Digite o {k}º valor numérico:')))
   if valor % 2 == 0:
        lista[0].append(valor)
   else:
        lista[1].append(valor)

print(f'A lista com valores pares e impares é {lista}')

lista[0].sort()
lista[1].sort()
print(f'Os valores pares em ordem crescente são {lista[0]}')
print(f'Os valores impares em ordem crescente são {lista[1]}')