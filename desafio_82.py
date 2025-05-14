lista = []
pares = []
impares = []
ans = ' '


while True:
    n = int(input('Digite um valor:'))
    if n in lista:
        print('Esse número já está na lista')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso')
    ans = input('Você quer continuar? [S/N]:').upper().strip()[0]
    if ans == 'N':
        break

for i, k in enumerate(lista):
    if k % 2 == 0:
        pares.append(k)
    else:
        impares.append(k)

print(f'A lista principal é {lista}')
print(f'A lista só com os números pares é {pares}')
print(f'A lista só com os números ímpares é {impares}')
