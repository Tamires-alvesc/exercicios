#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.No final mostra:
# 1 - a média de idade do grupo
# 2 - Qual o nome do homem mais velho
# 3 - quantas mulheres tem menos de 20 anos

lista_nome = []
lista_idade = []
lista_sexo = []

veio = []
women = []
cont_women = 0 

for k in range(0,4):
    dados = input('Entre com o nome, idade e sexo (M/F) separados por vírgula:')
    dados = dados.replace(' ','')
    lista_dados = dados.split(',')
    lista_nome.append(lista_dados[0])
    lista_idade.append(int(lista_dados[1]))
    lista_sexo.append(lista_dados[2])

    if len(veio) == 0 and lista_dados[2] == 'M':
        veio = lista_dados
    elif lista_dados[2] == 'M':
        if veio[1] < lista_dados[1]:
            veio = lista_dados

    if lista_dados[2] == 'F':
        women = lista_dados
        if int(women[1]) < 20:
            cont_women += 1



print(f'A média de idade do grupo é {sum(lista_idade)/len(lista_idade)}')

print(f'O nome do homem mais velho é {veio[0]} e ele tem {veio[1]} anos')

print(f'O número de mulheres com menos de 20 anos é {cont_women}')


#idade_max = max(lista_idade)

#index_lista = lista_idade.index(max(lista_idade))

#nome_veio = lista_nome[index_lista]
