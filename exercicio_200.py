import requests 
response = requests.get(
    url = "https://official-joke-api.appspot.com/random_joke"
)

print(response.json())

