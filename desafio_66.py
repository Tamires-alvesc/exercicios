n = cont = soma = 0

while True:
    n = int(input('Entre com um número inteiro [999 para parar]:\n'))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Foram digitados {cont} números e  a soma entre eles é {soma}')