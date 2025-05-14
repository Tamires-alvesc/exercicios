import requests

url = "https://pudim.com.br"

try:
    resposta = requests.get(url)
except:
    print('Não foi possível acessar o site')
else:
    print('Consegui acessar o site Pudim com sucesso!')
