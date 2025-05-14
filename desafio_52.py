n = int(input('Entre com um número inteiro:\n'))

primo = True

for k in range (1,n+1):
    if n % k == 0 and k != 1 and n != k:
       primo = False
       break

if primo:
    print('O número é primo')
else: 
    print('O número não é primo')


#n = int(input('Digite um número:'))

#tot = 0
#for c in range (1, n + 1):
#    if n % c == 0:
#       print('\033[33m', end = '')
#       tot += 1
#    else:
#        print('\033[31m', end = '')
#print(f'\n\033[m O número {n} foi divisível {tot}')
#if tot = 2:
#   print('E por isso ele é primo!')
#else:
#   print('E por isso ele não é primo!')