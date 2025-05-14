tupla2 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = ''
k = ''

while True: 
    n = int(input('Digite um número entre 0 e 20:'))
    if 0 <= n <= 20:
        print(f'Você digitou o número {tupla2[n]}')
    else:
        print('Tente novamente')

    k = input('Você quer continuar? [S/N]').strip().upper()[0]
    if k == 'N':
        break
    print('FIM')

