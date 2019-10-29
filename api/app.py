
import flask

from controllers.users import blueprint as users
## sempre deixar duas linhas em branco entre as import e o codigo

app = flask.Flask(__name__)

app.register_blueprint(users,url_prefix='/users')

## preferivel usar ' do que "
if __name__ == '__main__':
    app.run(host='0.0.0.0')
