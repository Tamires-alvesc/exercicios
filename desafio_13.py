km = float(input('Qual a quantidade de Km percorridos com o carro?'))

dias = int(input('Por quantos dias ficou alugado?'))

preço = km*0.15 + dias*60

print(f'O preço total da locação é de R${preço:.2f}')