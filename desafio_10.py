p = float(input('Insira o preço do produto: R$'))

d = float (input('Insira o desconto percentual: '))

pnovo = p*(1 - (d/100))

print(f'O preço com desconto de {d:.2f}% é {pnovo:.2f}')


