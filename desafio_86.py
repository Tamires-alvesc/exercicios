matriz = [[],[],[]]


for i, l in enumerate(matriz):
    linha = i + 1
    for k in range(0,3):
        coluna = k + 1
        a = int(input(f'valor [{linha},{coluna}]:'))
        l.append(a)
print(F'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')



# matriz = [[0,0,0], [0,0,0], [0,0,0]]
# for l in range(0,3):
#    for c in range(0,3):
#       matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
#print('-=' *30)
# for l in range(0,3):
#    for c in range(0,3):
#       print(f'[{matriz[l][c]:^5}]', end='')
#   print()