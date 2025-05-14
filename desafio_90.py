aluno = dict()
registro = list()


aluno['nome'] = str(input('Entre com o nome do aluno:'))
aluno['media'] = float(input('Entre com a média do aluno:'))

if aluno['media'] < 7:
    aluno['situ']  = 'REPROVADO'
else:
    aluno['situ'] = 'APROVADO'

registro.append(aluno.copy())

print(registro)

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
