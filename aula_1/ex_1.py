import requests


res = requests.get('https://gen-net.herokuapp.com/api/users/')
if res.status_code == 200:
    print(res.json())
else:
    print(res.text)
