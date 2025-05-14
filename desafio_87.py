
matriz = [[],[],[]]
soma = 0

for l in matriz:
    for k in range(0,3):
        l1 = int(input(f'valor {k}:'))
        if l1 % 2 == 0:
            soma += l1
        matriz[k].append(l1)
print(F'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')

tot = matriz[0][2] + matriz[1][2] + matriz[2][2]

print(f'A soma dos valores pares digitados é {soma}')
print(f' A soma de todos os valores da terceira coluna é {tot}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')