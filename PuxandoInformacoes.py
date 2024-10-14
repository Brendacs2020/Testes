import requests
import json

# Define o IP e o endpoint da API
ip = "http://10.0.0.1"
endpoint = "/#/login"
url = ip + endpoint

payload = {
    "data": {
        "username": "admin",
        "password": "admin"
    }
}

# Cabeçalhos da requisição (se a API exige cabeçalhos como Content-Type)
headers = {
    "Content-Type": "application/json"
}

# Faz a requisição POST enviando o JSON
response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    try:
        # Tenta converter a resposta em JSON
        response_json = response.json()
        print("Login bem-sucedido!")
        print("Resposta da API (JSON):", response_json)
    except ValueError:
        # Caso a resposta não seja JSON
        print("Resposta da API não está no formato JSON. Conteúdo recebido:")
        print(response.text)
else:
    print(f"Erro ao fazer login: {response.status_code}")
    print("Detalhes:", response.text)

#     #GET, POST, PUT, e DELETE