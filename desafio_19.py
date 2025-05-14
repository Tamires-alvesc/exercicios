nome = str(input('Digite seu nome completo:\n'))

#O nome com todas as letras maiúsculas:
print(f'O nome em maiúsculas é {nome.upper()}')

#O nome com todas as letras minúsculas:
print(f'O nome em minúsculas é {nome.lower()}')

#Quantas letras tem o nome sem contar os espaços:
print(f'O nome tem {len(nome) - nome.count(' ')} letras')

dividido = nome.split()


#Quantas letras tem o primeiro nome:
print(f'O primeiro nome tem {len(dividido[0])} letras')