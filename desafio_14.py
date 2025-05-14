import math

#num = float(input('Escreva um número:'))

#int_num = math.floor(num)

#print(f'A parte inteira de {num} é {int_num}')

num = input('Escreva um número:')

num_separated = num.split('.')

num_int = num_separated[0]

num_dec = num_separated[1]

print(num)