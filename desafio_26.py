v = float(input('Entre com a velocidade do carro em km/h:\n'))

if v>= 80:
    print(f'Você foi multado. A multa custará {7*(v-80)}')