n = int(input('Entre com um número:\n'))

k = 1
fat = n 

while k != n:
    fat = fat*(n-k)
    n = n - 1
print(f'O fatorial do número é {fat}')

#from math import factorial


# c = n
# f = 1
# print('Calculando {}! = '.format(n), end='')
# while c>0:
#   print('{}'.format(c), end='')
#   print(' x ' if c>1 else ' = ', end = '')
#   f *= c
#   c -= 1
#print('{}'.format(f))