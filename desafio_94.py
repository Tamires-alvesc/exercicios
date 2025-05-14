pessoa = dict()
cadastro = []
mulheres = []
velhos = []
num = 0
total = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Entre com o nome: '))
    while True:
        pessoa['sexo'] = str(input('Entre com o sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite somente M ou F')
        
    pessoa['idade'] = int(input('Entre com a idade: '))
    num += 1
    cadastro.append(pessoa.copy())
    while True:
        ans = str(input('Quer continuar?[S/N]')).upper()[0]
        if ans in 'SN':
            break
        else:
            print('Digite apenas S ou N')
    if ans == 'N':
        break

print(cadastro)


for e in cadastro:
    total += e['idade']
    if e['sexo'] == 'F':
        mulheres.append(e['nome'])

for e in cadastro:   
    if e['idade'] > total/num:
        velhos.append(e['nome'])


print(f'A média das idades do grupo é {total/num}')
print(f'As mulheres do grupo são {mulheres}')
print(f'As pessoas do grupo com idade acima da média são {velhos}')

#lista com todas as mulheres


#lista com todas as pessoas com idade acima da média