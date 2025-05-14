from datetime import date

cont = 0 

#datas = [2000, 2010, 1998, 2020, 1993, 2007, 2019]

#for k in datas


for k in range(0,7):
    ano = int(input(f'Escreva o ano de nascimento da {k}ª pessoa na forma AAAA:'))
    idade = date.today().year - ano
    if idade >= 21:
        cont = cont + 1
print(f'Das sete pessoas, {cont} já atingiram a maioridade e {7-cont} ainda não atingiram')