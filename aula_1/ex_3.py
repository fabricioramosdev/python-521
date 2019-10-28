import requests

url = 'https://gen-net.herokuapp.com/api/users/'
res =  requests.get(url)


if res.status_code == 200:
    pass
else:
    pass

