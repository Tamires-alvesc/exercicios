city = str(input('Qual o nome da sua cidade?\n')).strip()

city = city.upper()
if city.find('SANTO') == 0:
    print('O nome da cidade começa com SANTO')
else:
    print('O nome da cidade não começa com SANTO')


#print(city[:5].upper() == 'SANTO')