from fabric.api import run, local

def dump_data():
	local('python manage.py dumpdata companies --indent 4 > companies.json')
	local('python manage.py dumpdata contacts --indent 4 > contacts.json')
	local('python manage.py dumpdata auth.user --indent 4 > user.json')
	local('rm latech.db')

def load_data():
	local('python manage.py syncdb')
	local('python manage.py loaddata companies.json')
	local('python manage.py loaddata contacts.json')
	local('python manage.py loaddata user.json')
 
    
