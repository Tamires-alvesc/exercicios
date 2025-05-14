teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

povo = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(povo)
print(povo[3][0])

for p in povo:
    print(f'{p[0]} tem {p[1]} anos de idade')


povinho = list()
dado = list()

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    povinho.append(dado[:])
    dado.clear()

print(povinho)