#Criar um programa que faça o computador jogar Jokenpô com vc. (Pedra, papel e tesoura)

from random import randint

from time import sleep

opcoes = ["pedra","papel","tesoura"]

sua_escolha = int(input('Escreva sua opção: 1-pedra, 2-papel ou 3-tesoura\n'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)

escolha_pc = randint(0,2)

escolha_opcao = opcoes[escolha_pc]

if sua_escolha == 1 or sua_escolha == 2 or sua_escolha == 3:
    print(f'Você escolheu {opcoes[sua_escolha - 1]} e o computador escolheu {escolha_opcao} ')

    if escolha_pc == 0 and sua_escolha == 2:
        print("Papel ganha de pedra. Você venceu!")

    elif escolha_pc == 0 and sua_escolha == 3:
     print("Pedra ganha de tesoura. O computador venceu!")

    elif escolha_pc == 1 and sua_escolha == 1:
        print("Papel ganha de pedra. O computador venceu!")

    elif escolha_pc == 1 and sua_escolha == 3:
        print("Tesoura ganha de papel. Você venceu!")

    elif escolha_pc == 2 and sua_escolha == 1:
        print("Pedra ganha de tesoura. Você venceu!")

    elif escolha_pc == 2 and sua_escolha == 2:
        print("Tesoura ganha de papel. O computador venceu!")

    elif escolha_pc == sua_escolha - 1:
        print('EMPATE! Tente de novo')

else:
    print('Jogada inválida. Escolha novamente.')
