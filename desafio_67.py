

while True:
    x = int(input('Quer ver a tabuada de qual valor?:\n'))
    print('-'*15)
    if x < 0:
        print('Erro, número digitado é negativo')
        break
    for k in range (0,11):
        print(f'{x} x {k} = {x*k}')
    print('-'*15)