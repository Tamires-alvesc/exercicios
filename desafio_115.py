def cadastrar():
    with open("cadastros.txt", "a", encoding="utf-8") as arquivo:
        while True:
            nome = str(input('Entre com o nome:'))
            idade = int(input('Entre com a idade'))
            arquivo.write(f"Nome: {nome}, Idade: {idade}\n")
            ans = input('Quer continuar cadastrando pessoas?').upper().strip()[0]
            if ans == 'N':
                break 


def listar():




print('-'*40)
print('MENU PRINCIPAL')
print('-'*40)
print('1 - Ver pessoas cadastradas\n 2 -  Cadastrar nova pessoa\n 3 - Sair do sistema\n')
print('-'*40)

n = int(input('Sua Opção:'))

if n == 1:
    

