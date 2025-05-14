import datetime

ano = int(input('Digite seu ano de nascimento\n'))

idade = datetime.date.today().year - ano

if idade <= 9:
    print('Atleta Categoria Mirim')

elif  9 < idade <= 14:
    print('Atleta Categoria Infantil')

elif  14 < idade <= 19:
    print('Atleta Categoria Júnior')

elif 19 < idade <= 20:
    print('Atleta Categoria Sênior')

else:
     print('Atleta Categoria Master')