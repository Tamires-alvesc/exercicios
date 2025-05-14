salary = float(input('Qual o salário do funcionário? R$').replace(',','.'))

new_salary = 1.15*salary

print(f'O novo salário com reajuste de 15% será {new_salary:.2f}')