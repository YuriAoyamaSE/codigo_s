import requests

payload = {'key': 'value1', 'key2': 'value2'}

r = requests.post("https://httpbin.org/post", data=payload)

print(r.json())
print(r.text)
