import math

a = float(input('Qual a medida do cateto oposto do triângulo retângulo?'))

b = float(input('Qual a medida do cateto adjacente do triângulo retângulo?'))

alpha = math.atan(a/b)

hip = b/math.cos(alpha)

print(f'A hipotenusa do triângulo com catetos {a} e {b} vale {hip}')

#hip = math.hypot(a,b)