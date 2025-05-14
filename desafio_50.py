s = 0

for c in range (1,7):
    num = int(input(f'Digite o {c}º número:\n'))
    if num % 2 == 0:
        s = s + num
print(f'A soma dos valores pares é {s}')