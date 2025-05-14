cont_idade = cont_homens = cont_mu20 = 0

while True:

    idade = int(input('Qual a idade da pessoa?'))
    sexo = ' '
    ans = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo da pessoa? [M/F]')).upper().strip()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homens += 1
    if idade < 20 and sexo == 'F':
        cont_mu20 += 1
    while ans not in 'SN':
        ans = str(input('Quer continuar a cadastrar pessoas? [S/N]')).upper().strip()[0]
    if ans == 'N':
        break
print(f'Foram cadastradas {cont_idade} pessoas com mais de 18 anos, {cont_homens} homens, e {cont_mu20} mulheres com menos de 20 anos')

