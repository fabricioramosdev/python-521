
import flask


blueprint =  flask.Blueprint('users',__name__)


@blueprint.route('/', methods=['GET'])
def get_users():
    return 'get all users'


@blueprint.route('/', methods=['POST'])
def post_users():
    return 'post users'
      
       
@blueprint.route('/<userid>', methods=['GET'])
def get_users_by_id(userid):
    return f'get all users {userid}'


@blueprint.route('/<userid>', methods=['DELETE'])
def delete_users(userid):
    return f'delete user {userid}'


@blueprint.route('/<userid>', methods=['PUT'])
def put_users(userid):
    return f'put user {userid}'


@blueprint.route('/<userid>', methods=['PATCH'])
def patch_users(userid):
    return f'patch user {userid}'














