s = str(input('Digite o sexo da pessoa [M/F]:')).strip().upper()[0]

while s != 'M' and s != 'F':
    s = str(input('Dados inválidos. Digite novamente o sexo da pessoa [M/F]:')).strip().upper()
print(f'Informação recebida com sucesso - sexo {s}. FIM')