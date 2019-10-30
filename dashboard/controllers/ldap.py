import flask

blueprint =  flask.Blueprint('ldap',__name__)
@blueprint.route('/sign-in', methods=['GET','POST'])
def sign_in():

    print(flask.request.form.get('email'))
    context = {
        'public_route': True
    }
    return flask.render_template('ldap.html', context=context)