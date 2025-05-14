n1 = float(input('Entre com o primeiro valor:\n'))
n2 = float(input('Entre com o segundo valor:\n'))

e = 0

while e!= 5:
  
    e = int(input('Escolha a opção do menu: \n [1]-somar \n [2]-multiplicar \n [3]-maior \n [4]-novos números \n [5]-sair do programa \n' ))

    if e == 1:
       soma = n1 + n2
       print(f'A soma entre {n1} e {n2} é {soma}') 

    elif e == 2:
        mult = n1*n2
        print(f'A multiplicação entre {n1} e {n2} é {mult}') 

    elif e == 3:
      if n1 > n2:
          print(f'O maior número entre {n1} e {n2} é {n1}')
      elif n2 > n1:
          print(f'O maior número entre {n1} e {n2} é {n2}')
      else:
          print('Os dois números são iguais')

    elif e == 4:
        print('Digite novos números:\n')
        n1 = float(input('Entre com o primeiro valor:\n'))
        n2 = float(input('Entre com o segundo valor:\n'))
        e = int(input('Escolha a opção do menu: \n [1]-somar \n [2]-multiplicar \n [3]-maior \n [4]-novos números \n [5]-sair do programa \n' ))
    else:
        ('Opção inválida. Tente novamente')
print('Você escolheu sair.FIM')