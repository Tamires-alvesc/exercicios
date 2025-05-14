
#n = cont = soma = 0

n = 0

cont = 0

soma = 0

n = int(input('Entre com um número inteiro [999 para parar]:\n'))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Entre com um número inteiro [999 para parar]:\n'))

print(f'Foram digitados {cont} números e  a soma entre eles é {soma}')

#flag é uma condição de parada