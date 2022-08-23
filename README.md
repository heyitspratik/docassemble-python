# docassemble-python


Docassemble using Django Framework

## create virtual environment using below command and activate the same
```
python3 -m venv venv
```
## required installments
install all the python packages mentioned in requirements.txt file

## create django project and make an app inside it
```
django-admin startproject projectname
python manage.py startapp appname
```

## Database Migration
Use below command for migration of tables
```
python manage.py makemigrations
python manage.py migrate
```
## create superuser to access django admin panel
```
python manage.py createsuperuser
```
## starting development server using below command
```
python manage.py runserver
```
which will run on (http://127.0.0.1:8000/first-question/)
