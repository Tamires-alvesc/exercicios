a_0 = float(input('Escreva o primeiro termo da PA:'))

r = float(input('Escreva a razão:'))

for k in range(0,10):
    a_k = a_0 + k*r
    print(f'Termo a_{k}: {a_k:.1f}')
