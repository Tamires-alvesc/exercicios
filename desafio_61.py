a_1 = float(input('Entre com o primeiro termo:\n'))

r = float(input('Entre com a razão:\n'))

n = 1

while n < 11:
    a_n = a_1 + (n-1)*r

    print(f'Termo a_{n} = {a_n}')

    n = n + 1
    

#print('Gerador de PA')
#print('-='*10)
#primeiro = int(input('Primeiro termo:'))
#razão = int(input('Razão da PA:'))
#termo = primeiro
#cont = 1
#while cont <= 10:
    #print('{} > '.format(termo), end='')
    #termo += razão
    #cont += 1
#print('FIM')