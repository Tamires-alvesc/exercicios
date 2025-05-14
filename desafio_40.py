n1 = int(input('Entre com a primeira nota:\n'))
n2 = int(input('Entre com a segunda nota:\n'))

m = (n1+n2)/2

if m < 5:
    print(f'Sua média foi {m}, que é inferior a 5. Reprovado')

elif 5 <= m <=  6.9:
    print(f'Sua média foi {m}, que está entre 5 e 6.9. Irá para recuperação')

else:
    print(f'Sua média foi {m}, maior ou igual a 7. Aprovado')