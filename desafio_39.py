import datetime

ano = int(input('Qual o ano de nascimento?\n'))

sexo = input('Qual o sexo?\n 1-feminino\n 2-masculino\n')

idade = datetime.date.today().year - ano

if sexo == 1:
    print('Você é do sexo feminino, não precisa se alistar.')
if idade < 18:
    print(f'Você ainda irá se alistar. Sua idade é {idade} anos e faltam {18-idade} anos para o alistamento.')

elif idade > 18:
    print(f'Já passou do tempo de se alistar. Sua idade é {idade} anos e passaram {idade-18} anos a época de alistamento! Verifique sua situação.')

elif idade == 18:
    print(f'Você tem {idade} anos. É hora de se alistar!')