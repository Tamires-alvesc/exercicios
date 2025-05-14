#num = str(input('Digite um número entre 0000 e 9999:\n'))

#print('unidade', num[3])

#print('dezenas', num[2])

#print('centenas', num[1])

#print('milhares', num[0])


num2 = int(input('Digite um número entre 0000 e 9999:\n'))

print('unidade', num2 - (num2//10)*10)

print('dezenas', num2//10 - (num2//100)*10)

print('centenas', num2//100 - (num2//1000)*10)

print('milhares', num2//1000)