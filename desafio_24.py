name = str(input('Digite seu nome:\n')).strip()

name = name.split(' ')

print(f'O primeiro nome é {name[0]}')

k = int(len(name))

t = k-1

print(f'O último nome é {name[t]}')

#print(f'O último nome é {name[-1]}')
