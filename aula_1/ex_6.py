
import requests
import ex_4
url = 'https://gen-net.herokuapp.com/api/users'

def delete_user(user):
    requests.delete(url+'/'+str(user.get('id')))


def verify_password(email, password):
    res =  requests.post(url+'/auth',{'email':email, 'password':password})
    return res.status_code == 200


if __name__ == "__main__":

    email = input('Digite seu e-mail:\n')
    password =  input('Digite sua senha:\n')
    
    user = ex_4.get_user_by_email(email)
    if user and verify_password(email, password):
        delete_user(user)
        print('Usuário removido com sucesso')
    else:
        print('Falha na operação')

