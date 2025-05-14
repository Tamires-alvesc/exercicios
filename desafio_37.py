n = int(input('Digite um número inteiro:\n'))

b = int(input('Escolha a base de conversão: \n1 - binário\n2 - octal \n3 - hexadecimal\n Sua opção:'))

#if b == 1:
#       while r > 0:
#        r = n % 2 
#        lista = []
#        lista.append(r)
#        lista.append(0)
#    lista.reverse()
#    resultado = join.lista()
#print(f'O número em binário é {resultado}')

#elif b == 2:



if b == 1:
    print(f'O número em binário é {bin(n)[2:]}')

elif b == 2:
    print(f'O número em octal é {oct(n)[2:]}')

elif b == 3:
    print(f'O número em hexadecimal é {hex(n)[2:].upper()}')

else:
    print('Número digitado não confere. Tente novamente')