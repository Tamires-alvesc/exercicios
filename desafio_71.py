#valor = int(input('Qual o valor a ser sacado?\nR$'))
#c = valor//50
#v = (valor % 50)//20 
#d = ((valor % 50)%20)//10
#u = ((valor % 50)%20)%10
#print(f'Serão entregues {c} cédulas de R$50, {v} cédulas de R$20, {d} cédulas de R$10 e {u} cédulas de R$1')

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? \nR$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV!')
