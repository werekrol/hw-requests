import requests


TOKEN = ''
response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload/',
                        params={'path': 'test.txt'},
                        headers={'Authorization': f'OAuth {TOKEN}'})
print(response.status_code)
print(response.json())
href = response.json()['href']
with open('test.txt') as f:
    requests.put(href, files={'file': f})