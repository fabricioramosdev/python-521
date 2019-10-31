import flask
import jenkins


blueprint = flask.Blueprint('jenkins', __name__)

def get_jenkins_connection():

    url = 'http://localhost:8080'

    username = 'admin' 
    password = '4linux'

    try:
        return jenkins.Jenkins(url, username, password)
    except:
        return None

def get_jobs():

    conn = get_jenkins_connection()

    if not conn:
        return []

    def get_job_status(j):
        if not j.get('firstBuild'):
            return 'Nunca buildou'
        elif j.get('lastSuccessfulBuild').get('number') == (j.get('nextBuildNumber')-1):
            return 'Sucesso'
        else:
            return 'Falha'
            
    def fn(j):
        return {
            'name': j.get('fullName'),
            'status': j.get('healthReport')[0].get('iconUrl'),
            'last_execution': get_job_status(j)
        }

    jobs = [ 
        conn.get_job_info(j.get('fullname')) for j in conn.get_all_jobs() 
    ]

    return [ fn(j) for j in jobs ]

@blueprint.route('/jenkins', methods=[ 'GET', 'POST' ])
def jenkins_action():
    context = {
        'route':'jenkins',
        'jobs': get_jobs()
    }
    print(context)
    return flask.render_template('jenkins.html', context=context)

@blueprint.route('/jenkins/<jobname>/run', methods=[ 'GET', 'POST' ])
def jenkins_run_action(jobname):

    conn = get_jenkins_connection()

    if conn:
        conn.build_job(jobname)

    return flask.redirect('/jenkins')

