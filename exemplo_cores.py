
from math import sqrt

from math import pow


#\033[0:30:41m

#\033[4:33:44m

#\033[1:35:43m

#\033[0:30:42m

#\033[m

#\033[7:30m

print('\033[4;30;45mOlá, mundo\033[m')

print('\033[7;33;44mOlá, mundo\033[m')

nome = 'Guanabara'
cores = {'limpa':'\033[m', 'azul':'\033[34m'}
         
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m',nome,'\033[m'))