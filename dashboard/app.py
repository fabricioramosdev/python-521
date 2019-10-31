import os
import flask
import dotenv

from controllers.docker_routes import blueprint as docker
from controllers.gitlab import blueprint as gitlab
from controllers.jenkins_routes import blueprint as jenkins
from controllers.ldap import blueprint as ldap
dotenv.load_dotenv()

app =  flask.Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY') or 'secret'
app.register_blueprint(docker)
app.register_blueprint(gitlab)
app.register_blueprint(jenkins)
app.register_blueprint(ldap)


@app.route('/',methods=['GET'])
def get_home():
    return flask.redirect('/docker')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')