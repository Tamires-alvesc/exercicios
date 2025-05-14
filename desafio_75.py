
tupla = ()
pares = ()
for k in range (0, 4):  
    n = int(input('Digite um número:'))
    tupla = tupla + (n,)
print(f'Os valores digitados foram {tupla}')

print(f'O número 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O primeiro valor 3 apareceu na posição {tupla.index(3)+1}')
else:
    print('Não há o número 3 nessa tupla')

for x in tupla:
    if x % 2 == 0:
        pares = pares + (x,)
print(f'Os números pares são {pares}')

#núm = (int(input('Digite um número:')), int(input('Digite outro número:')), int(input('Digite mais um número:')), int(input('Digite o último número:')))
#print(f'Você digitou os valores {núm}')