a_1 = float(input('Entre com o primeiro termo:\n'))

r = float(input('Entre com a razão:\n'))

n = 1

while n < 11:
    a_n = a_1 + (n-1)*r

    print(f'Termo a_{n} = {a_n}')
    
    n = n + 1

ans1 = str(input('Você quer que mostre mais termos? [S/N] ')).upper()


if ans1 == 'S':
    ans2 = int(input('Quantos termos a mais?'))
    if ans2 != 0:
        while 11 <= n < 11 + ans2:
            a_n = a_1 + (n-1)*r
            print(f'Termo a_{n} = {a_n}')
            n = n + 1
    else:
        print('FIM')
elif ans1 == 'N':
    print('FIM')
else:
    print('Resposta inválida. Tente novamente')

