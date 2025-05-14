preco = float(input('Qual o preço normal do produto?\n'))

forma_pag = int(input('Entre com a forma de pagamento: 1 - dinheiro à vista , 2 - cartão à vista, 3 - duas vezes no cartão,  4 - em 3 ou mais vezes no cartão\n'))


if forma_pag == 1:
    precof = preco*0.9
    print(f'Você ganhou 10 por cento de desconto. Preço final de R${precof}')

elif forma_pag == 2:
    precof = preco*0.95
    print(f'Você ganhou 5 por cento de desconto. Preço final de R${precof}')

elif forma_pag == 3:
    print(f'Você irá pagar o preço normal, de R${preco} em 2 parcelas de {preco/2} SEM JUROS')

elif forma_pag == 4:
    precof = preco*1.2
    totalparc = int(input('Quantas parcelas?'))
    print(f'Você irá pagar o preço com 20 por cento de juros, de R${precof}, em {totalparc} parcelas de {precof/totalparc}, COM JUROS')

else:
    print('Forma de pagamento não identificada. Tente novamente.')