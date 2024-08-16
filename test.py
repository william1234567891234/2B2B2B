import requests

url = "http://localhost:81"
response = requests.get(url)

assert response.status_code == 200
print("Teste passou: Página carregou corretamente.")
