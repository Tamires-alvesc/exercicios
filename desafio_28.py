d = float(input('Qual a distância da viagem em Km?\n'))

if d<= 200:
    print(f'A viagem custará {0.5*d} reais')
else:
    print(f'A viagem custará {0.45*d} reais')
    
#preço = d*0.50 if d <= 200 else d*0.45