
import flask
import docker
from services.authentication import login_required

blueprint =  flask.Blueprint('docker',__name__)


def get_containers():
    try:
        client = docker.DockerClient()     

        def fn(c):
            return {
                'id':c.short_id,
                'status':c.status,
                'image': c.image.tags[0] if len(c.image.tags) else 'sem tag'
            }

        return [fn(c) for c in client.containers.list(all=True)]


    except docker.errors.DockerException:
        return []


@blueprint.route('/docker', methods=['GET','POST'])
@login_required
def docker_action():

    context = {
        'route':'docker',
        'containers': get_containers()
    }
    return flask.render_template('docker.html', context=context)


@blueprint.route('/docker/<id>/start', methods=['GET'])

def docker_start_container_action(id):
    try:
        client = docker.DockerClient()
        container = client.containers.get(id)
        if container:
            container.start()
    except docker.errors.DockerException:
        pass
    finally:
        return flask.redirect('/docker')


@blueprint.route('/docker/<id>/stop', methods=['GET'])
def docker_stop_container_action(id):
    try:
        client = docker.DockerClient()
        container = client.containers.get(id)
        if container:
            container.stop()
    except docker.errors.DockerException:
        pass
    finally:
        return flask.redirect('/docker')

    
