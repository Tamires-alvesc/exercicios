lista = []
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
lista.sort()
print(lista)
print(f'Os valores digitados foram {lista}')