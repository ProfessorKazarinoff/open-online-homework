# Deployment

## Heroku

Use git to keep track of changes

### Install and add the Heroku Django package

```text
pip install django-heroku
```

Inside of settings.py

```text
# at the top in the imports
import django_heroku

# at the bottom
django_heroku.settings(locals())
```

### Add 3 required files to project root

 * requirements.txt (```pip freeze > requirements.txt```)
 * runtime.txt (```python-3.7.6```)
 * Procfile (```web: gunicorn open_online_homework.wsgi --log-file -```)

### Install Heroku CLI

Install the Heroku CLI

### Git add, commit, push

```text
git add .
git commit -m "deployment on heroku"
git push origin master
```

### Push to Heroku

```text
heroku login
heroku create my_app_name
git push heroku master
heroku open
```

### Migrate the database on Heroku

```text
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## Docker

Working on it...

## Digital Ocean

Working on it...

## AWS

Working on it...
