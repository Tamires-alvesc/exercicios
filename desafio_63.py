n = int(input('Entre com quantos termos você deseja mostrar:\n'))

a_0 = 0

a_1 = 1

cont = 0

print(f'Imprimindo os {n} primeiros termos da sequência de Fibonacci:')

while cont < n:
    a_0 , a_1 = a_1 , a_0 + a_1
    print(f'Termo {cont+1}: {a_0}')
    cont += 1


#print('Sequência de Fibonacci')
#n = int(input('Quantos termos você quer mostrar?'))
#t1 = 0
#t2 = 1
#print('~'*30)
#print('{} > {}'.format(t1, t2), end='')
#cont = 3
#while cont <= n:
#   t3 = t1 + t2
#   print(' > {}'.format(t3), end='')
#   t1 = t2
#   t2 = t3
#   cont += 1
#print(' > FIM')