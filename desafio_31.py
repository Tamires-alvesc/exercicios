s = float(input('Qual o seu salário?\n'))

if s > 1250:
    print(f'O valor do aumento será de {0.1*s}, e o novo salário total fica {1.1*s}')
else:
    print(f'O valor do aumento será de {0.15*s}, e o salário total fica {1.15*s}')