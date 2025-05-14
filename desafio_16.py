import math

x = float(input('Qual o ângulo em graus?'))

alpha = (3.1415/180)*x  #ou alpha = math.radians(x)

print(f'O seno vale {math.sin(alpha):.2f}, o cosseno vale {math.cos(alpha):.2f} e a tangente vale {math.tan(alpha):.2f}')