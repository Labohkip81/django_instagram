import os

from fabric import task

PROJECT_DIR = '/home/projects/django_instagram'
VIRTUALENV_ACTIVATE_CMD = 'source /home/projects/django_instagram/venv/bin/activate'
USERNAME = os.environ.get('username')
HOSTNAME = os.environ.get('host')
hosts = [f'{USERNAME}@{HOSTNAME}']


@task(hosts=hosts)
def deploy(connection):
    connection.put(
        'docker/docker-compose.yml',
        f'{PROJECT_DIR}/docker-compose.yml'
    )
    connection.put(
        'docker/nginx.conf',
        f'{PROJECT_DIR}/nginx.conf'
    )
    connection.put(
        'docker/gunicorn.conf',
        f'{PROJECT_DIR}/gunicorn.conf'
    )
    connection.run(
        f'cd {PROJECT_DIR}; docker-compose pull && docker-compose down && docker-compose up -d'
    )
