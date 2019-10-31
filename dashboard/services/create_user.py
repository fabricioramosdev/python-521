import ldap3
import hashlib


user ='cn=admin,dc=dexter,dc=com,dc=br'
password='4linux'                   

server =  ldap3.Server('ldap://localhost:389')
connection = ldap3.Connection(server, user, password, auto_bind=True)

if __name__ == '__main__':
    name =  input('Digite seu nome:')
    lastname = input('Digite seu sobrenome:')
    email = input('Digite seu e-mail:')
    password =  input('Digite sua senha:')

    user = {
        'cn':name,
        'sn':lastname,
        'mail': email,
        'uidNumber':'1',
        'gidNumber':'1',
        'uid':email,
        'homeDirectory': '/home/{}/{}'.format(
            name.lower(), lastname.split(' ')[0].lower()
        ),
        'userPassword':hashlib.sha256(password.encode()).hexdigest()   
    }

    objectClass = [
        'top',
        'person',
        'organizationalPerson',
        'inetOrgPerson',
        'posixAccount'
    ]

    cn = f'uid={email},dc=dexter,dc=com,dc=br'
    if connection.add(cn,objectClass, user):
        print('Usuário cadastro com sucesso')
    else:
        print('Falha ao cadastrar novo usuárop')
