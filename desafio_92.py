#aposenta depois de 35 anos de trabalho

from datetime import date  #ou from datetime import datetime

pessoa = dict()

pessoa['nome'] = str(input('Entre com o nome da pessoa:'))

ano_nasc = int(input('Entre com o ano de nascimento da pessoa:'))
year = date.today().year  #ou datetime.now().year
pessoa['idade'] = year - ano_nasc

pessoa['ctps'] = int(input('Insira o número da carteira de trabalho: (0 p/ não tem)'))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Qual o ano de contratação?'))
    pessoa['salário'] = float(input('Qual o salário? R$ '))
    tempo_serviço = year - pessoa['contratação']
    pessoa['aposentadoria'] = pessoa['idade'] + 35 - tempo_serviço
else:
    print('Pessoa não trabalha')

print(pessoa)

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')