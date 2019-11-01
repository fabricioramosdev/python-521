import flask
import ldap3
import hashlib

blueprint =  flask.Blueprint('ldap',__name__)

def get_ldap_connection():
    
    user ='cn=admin,dc=dexter,dc=com,dc=br'
    password='4linux' 
    server =  ldap3.Server('ldap://localhost:389')

    try:
        return ldap3.Connection(server, user, password, auto_bind=True)
    except:
        print('erro')
        pass

def find_user_by_email(email, conn):    
      
    conn.search(
        'uid={},dc=dexter,dc=com,dc=br'.format(email),
        '(objectClass=person)',
        attributes=[
            'sn',
            'userPassword'
        ]
    )

    return conn.entries[0] if len(conn.entries) > 0 else None

def verify_password(user, password):
    print(50*'@')
    saved_password = user.userPassword.value.decode()
    return hashlib.sha256(password.encode()).hexdigest()


@blueprint.route('/sign-in', methods=['GET','POST'])
def sign_in():

    conn = get_ldap_connection()
    
    if conn and flask.request.method == 'POST':
       
        email = flask.request.form.get('email')
        password = flask.request.form.get('password')

        # encontrar o usuário pelo e-mail no ldap
        user = find_user_by_email(email, conn)    

        print(user)

        if user and verify_password(user, password):
            flask.session['authenticated'] = True
            return flask.redirect('/')
  
    context = {
        'public_route': True
    }
    return flask.render_template('ldap.html', context=context)


@blueprint.route('/sign-out', methods=['GET','POST'])
def sign_out():

    try:
        del flask.session['authenticated']
    except KeyError:
        pass
    return flask.redirect('/')