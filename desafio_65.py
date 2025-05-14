
soma = 0 
ans = ''
numeros = []

while ans in 'sS':

    n = int(input('Entre com um número inteiro:\n'))

    ans = str(input('Você quer continuar a digitar valores? [S/N]\n')).upper().strip[0]
    soma += n
    numeros.append(n)


print(f'A média entre os valores digitados é {soma/len(numeros)}. O maior valor lido foi {max(numeros)} e o menor foi {min(numeros)}')

