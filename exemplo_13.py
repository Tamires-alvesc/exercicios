pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) #aparece como lista composta com tuplas

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')


#criar dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])