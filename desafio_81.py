lista = []
ans = ' '
cont = 0

while True:
    n = int(input('Digite um valor:'))
    if n in lista:
        print('Esse número já está na lista')
    else:
        lista.append(n)
        cont += 1
        print('Valor adicionado com sucesso')
        ans = input('Você quer continuar? [S/N]:').upper().strip()[0]
        if ans == 'N':
            break
    
lista.sort(reverse = True)
print(f'Foram digitados {cont} números')
print(f' A lista ordenada de forma decrescente é {lista}')
cont_5 = lista.count(5)
print(f'O valor 5 aparece {cont_5} vezes na lista')