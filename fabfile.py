from fabric.api import local

def prepare_deployment(branch_name):
    local('python manage.py test sigma_intro')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)

from fabric.api import lcd

def deploy(local_path, _port):
    with lcd(local_path):
        local('git pull')
        local('python manage.py migrate sigma_intro')
        local('python manage.py test sigma_intro')
        # Will remove this and put gunicorn with gevent in future
        # That itself will run as a daemon program
        local('python manage.py runserver %s' % _port)
