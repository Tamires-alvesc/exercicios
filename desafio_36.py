valor = float(input('Qual o valor da casa?\n'))

salario = float(input('Qual o seu salário?\n'))

anos = float(input('Em quantos anos irá pagar?\n'))

parcela = valor/(12*anos)

if parcela > 0.3*salario:
    print(f'A parcela é de {parcela:.2f} reais e excede 30 por cento do salário. Empréstimo não autorizado!.')

elif parcela == 0.3*salario:
    print(f'A parcela é de {parcela:.2f} reais e é igual a 30 por cento do salário. Será feita uma análise mais apurada')

else:
    print(f'Parcela de {parcela:.2f} reais, menor que 30 por cento do salário. Empréstimo aprovado!')

