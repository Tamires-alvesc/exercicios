total = mais_mil = quant = menor = maior = 0
nome_barato = ''

while True:

    nome = str(input('Qual o nome do produto?\n'))
    preco = float(input('Qual o preço do produto?\n'))
    total += preco
    quant += 1
    ans = ' '
    if preco > 1000:
        mais_mil += 1

    if quant == 1:
        maior = menor = preco
        nome_barato = nome
    else: 
        if preco > maior:
            maior = preco
        if preco < menor:
            menor = preco
            nome_barato = nome
    while ans not in 'SN':
        ans = str(input('Deseja continuar [S/N]?')).upper().strip()[0]
    if ans == 'N':
        break
print(f'O total gasto foi de R${total:.2f}. {mais_mil} produtos custam mais de 1000 reais. O produto mais barato custa {menor} e seu nome é {nome_barato}')
print('{:-^40}'.format('FIM DO PROGRAMA'))
