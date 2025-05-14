def leiaInt(k):
    try:
        n = int(input(k))
    except(ValueError,TypeError):
        print('\033[0:31mErro. Não é um valor numérico inteiro\033[m') 
    except(KeyboardInterrupt):
        print('O usuário preferiu não informar os dados!')
    else:
        print(f'Inteiro {n} lido com sucesso!')
           
        
n = leiaInt('Digite um número inteiro:')


def leiaFloat(k = ' '):
    try:
        n = float(input(k).replace(',','.'))
    except(ValueError,TypeError):
        print('\033[0:31mErro. Não é um valor numérico flutuante\033[m') 
    except(KeyboardInterrupt):
        print('O usuário preferiu não informar os dados!')
    else:
        print(f'Flutuante {n} lido com sucesso!')
           

x = leiaFloat('Digite um número flutuante:')