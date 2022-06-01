import requests

gatinho_200 = requests.get("https://http.cat/200")

with open("200.jpeg", 'wb') as file:
    for gato in gatinho_200:
        file.write(gato)

print(f"Headers: {gatinho_200.headers}")
print(f"Status code: {gatinho_200.status_code}")
print(f"objeto: {gatinho_200}")
