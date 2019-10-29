
import flask
from models.users import  User


blueprint =  flask.Blueprint('users',__name__)


@blueprint.route('/', methods=['GET'])
def get_users():
    users = User.get_all_users()
    return flask.jsonify([u.to_json() for u in users])


@blueprint.route('/', methods=['POST'])
def post_users():

    required_fields = ['name', 'email', 'password']
    for field in required_fields:
        if field not in flask.request.json:
            return flask.jsonify({
                'error': f'{field} is requerid'
            }), 400

    user = User(**flask.request.json)
    
    if User.find_by_email(user.email):
        return flask.jsonify({
            'error': f'email already exists'
        }), 400

    user.save()
    
    return flask.jsonify(
        User.find_by_email(user.email).to_json()
    )


@blueprint.route('/<userid>', methods=['GET'])
def get_users_by_id(userid):
    user = User.find_by_id(userid)
    if not user:
        return flask.jsonify({
            'erro':'user not found'
        })
    return flask.jsonify(
        User.find_by_email(user.email).to_json()
    )


@blueprint.route('/<userid>', methods=['DELETE'])
def delete_users(userid):
    user = User.find_by_id(userid)
    if not user:
        return flask.jsonify({
            'erro': 'user not found'
        }), 404

    user.remove(userid)
    return f'delete user {userid}'


@blueprint.route('/<userid>', methods=['PUT'])
def replace_users_by_id(userid):
    user = User.find_by_id(userid)
    if not user:
        return flask.jsonify({
            'erro': 'user not found'
        }), 404

    opts = {
        '_id':user._id,
        'name':None,
        'email': None,
        'password':None
    }
    
    opts.update(**flask.request.json)
    user =  User(**opts)
    user.save()
    return flask.jsonify(
        User.find_by_id(userid).to_json()
    )

  
@blueprint.route('/<userid>', methods=['PATCH'])
def patch_users(userid):
    user = User.find_by_id(userid)
    if not user:
        return flask.jsonify({
            'erro': 'user not found'
        }), 404
    
    opts = {
        '_id':user._id,
        'name':user.name,
        'email': user.email,
        'password':user.password
    }
    
    opts.update(**flask.request.json)
    user =  User(**opts)
    user.save()
    
    return flask.jsonify(
        User.find_by_id(userid).to_json()
    )
