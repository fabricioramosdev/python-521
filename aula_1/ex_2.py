"""
Criar uma aplicação para cadastrar na api
solicitar os dados e informar se o usuário foi cadastrado com sucesso
"""
import requests


name =  input("Digite seu nome:\n")
email = input("Digite seu email:\n")
password = input("Digite sua senha:\n")
url = 'https://gen-net.herokuapp.com/api/users/'
res = requests.post(url ,{"name":name, \
                    "email":email, "password":password})


if res.status_code == 200:
    new_user = res.json()   
    print(f'Usuário cadastrado com sucesso ID: {new_user.get("id")}')
else:
    print(res.text)



