"""
Função que recebe como parametreo um email
e retorna se um usuário foi encontrado ou não None
"""
import requests

def get_user_by_email(email):

    url = 'https://gen-net.herokuapp.com/api/users/'
    res = requests.get(url, params={'email':email})

    if res.status_code == 200:
        try:
            return res.json()[0]
        except IndexError:
            pass
    return None

if __name__ == "__main__":

    email =  input('Digite seu email:\n')
    res = get_user_by_email(email)

    if res:
        print(res.get('name'))
    else:
        print('Usuário não encontrado')

   

