peso = float(input('Qual seu peso em kg?\n'))

altura =  float(input('Qual sua altura em m?\n'))

imc = peso/(altura**2)

if imc < 18.5:
    print(f'Seu IMC é {imc}.Você está abaixo do peso')

elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc},. Você está no peso ideal')

elif 25 <= imc < 30:
    print(f'Seu IMC é {imc},. Você está com sobrepeso')

elif 30 <= imc <= 40:
    print(f'Seu IMC é {imc},. Você está com obesidade')

else:
    print(f'Seu IMC é {imc}. Você está com obesidade mórbida ')





