
import flask

from controllers.users import blueprint as users
## sempre deixar duas linhas em branco entre as import e o codigo

app = flask.Flask(__name__)

app.register_blueprint(users,url_prefix='/users')

@app.route('/hello-word', methods=['GET'])
def get_hello_word():
    return flask.jsonify({
        'messsage':'hello, world.'
    })

## preferivel usar ' do que "
if __name__ == '__main__':
    app.run()
