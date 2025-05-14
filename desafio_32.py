a = float(input("Primeiro segmento:"))
b = float(input("Segundo segmento:"))
c = float(input("Terceiro segmento:"))

#triangulo = [a,b,c]

#triangulo.sort()

#triangulo[0] + triangulo[1]> triangulo[2]

if a<b+c and b<a+c and c<a+b:
    print('Essas retas podem formar um triângulo!')
else:
    print('Ops.Essas retas não podem formar um triângulo!')