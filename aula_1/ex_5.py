"""
Função que recebe como parametreo um email
e retorna se um usuário foi encontrado ou não None
"""
import requests
import ex_4

url = 'https://gen-net.herokuapp.com/api/users'


def change_password(user):
    password =  input('Digite sua nova senha:\n')

    user.update({
        'password':password
    })

    res = requests.put(url+'/'+str(user.get('id')) ,json=user)
    
    if res.status_code == 200:
        print(f'Sua senha foi alterada com sucesso {user.get("name")}')
    else:
        print('Erro ao tentar alterar senha.')


email =  input('Digite seu email:\n')
user = ex_4.get_user_by_email(email)

if user:
    change_password(user)    
else:
    print('Usuário não encontrado')
