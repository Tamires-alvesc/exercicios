n1 = float(input('Entre com o primeiro número:\n'))
n2 = float(input('Entre com o segundo número:\n'))
n3 = float(input('Entre com o terceiro número:\n'))

if n1>n2>n3 or n1==n2>n3:
    print(f'{n1} é o maior número e {n3} é o menor')

if n1>n3>n2 or n1==n3>n2:
    print(f'{n1} é o maior número e {n2} é o menor')

if n2>n1>n3:
    print(f'{n2} é o maior número e {n3} é o menor')

if n2>n3>n1 or n2==n3>n1:
    print(f'{n2} é o maior número e {n1} é o menor')

if n3>n2>n1:
    print(f'{n3} é o maior número e {n1} é o menor')

if n3>n1>n2:
    print(f'{n3} é o maior número e {n2} é o menor')

if n1==n2==n3:
    print('Os três números são iguais')