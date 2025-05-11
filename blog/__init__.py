import requests

res = requests.get('https://jsonplaceholder.typicode.com/posts')

if res.status_code == 200:
    data = res.json()
    print(data)
        
else:
    print(f'Erro: {res.status_code}')