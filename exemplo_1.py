c = input('Digite algo:\n')
print('É numérico?', c.isnumeric()) 
print('É alfabético?', c.isalpha())
print('É alfanumérico?', c.isalnum())
print('Só tem espaços?', c.isspace())
print('É maiúsculo?', c.isupper())
print('É minúsculo?', c.islower())
print('Está capitalizada?', c.istitle())

print('O tipo primitivo é', type(c))

if c.isalnum() == True:
    tipo = 'alfanumérica'
elif c.isalpha() == True:
    tipo = 'alfabética'
elif c.isnumeric() == True:
    tipo = 'numérica'
else:
   tipo = 'outra classificação'


print(f'A coisa digitada é {tipo}\n')