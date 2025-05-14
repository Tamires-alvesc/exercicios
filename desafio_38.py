n1 = int(input('Entre com o primeiro número:\n'))
n2 = int(input('Entre com o segundo número:\n'))

if n1 > n2:
    print(f'O primeiro valor é {n1} e é o maior número')

elif n2 > n1:
    print(f'O segundo valor é {n2} é o maior número')

else:
    print('Não existe valor maior. Os dois números são iguais')