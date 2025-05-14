a = float(input("Primeiro segmento:"))
b = float(input("Segundo segmento:"))
c = float(input("Terceiro segmento:"))


if a<b+c and b<a+c and c<a+b:
    print('Essas retas podem formar um triângulo!')
    if a == b == c:
        print(f'Os lados são iguais e o Triângulo é equilátero')
    elif a == b != c or b == c != a or a == c !=b:
        print(f'Dois dos lados são iguais e o Triângulo é isósceles')
    else:
        print('Todos os lados são diferentes e o triângulo é escaleno')
#ou elif r1 != r2 != r3 != r1 para o escaleno

else:
    print('Ops.Essas retas não podem formar um triângulo!')

