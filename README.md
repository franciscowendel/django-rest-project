# django-rest-app

_A Django project working with some API using DRF (Django Rest Framework) in it._

__Como executar o projeto:__

1. Caso não tenha o _pipenv_ instalado:
```console
pip install pipenv
pipenv sync -d
```

<br>

2. Caso tenha o _pipenv_ instalado:
```console
pipenv sync -d
```

<br>

3. Crie o arquivo _.env_ e dentro deste crie as seguintes variáveis de ambiente:
- DEBUG=True
- ALLOWED_HOSTS=localhost,127.0.0.1
- SECRET_KEY=minhachave

<br>

4. Faça a migração dos dados do projeto digitando os seguintes comandos:
```console
pipenv run python manage.py makemigrations

pipenv run python manage.py migrate
```
<br>

5. Crie um superusuário:
```console
pipenv run python manage.py createsuperuser
```
<br>

6. Rode o servidor:
```console
pipenv run python manage.py runserver
```

<br>

7. Entre no _admin_:
   - <http://127.0.0.1:8000/admin/>

<br>

8. Use o projeto.

<br>

[![Build Status](https://www.travis-ci.com/franciscowendel/django-rest-app.svg?branch=main)](https://www.travis-ci.com/franciscowendel/django-rest-app)
[![Updates](https://pyup.io/repos/github/franciscowendel/django-rest-app/shield.svg)](https://pyup.io/repos/github/franciscowendel/django-rest-app/)
[![Python 3](https://pyup.io/repos/github/franciscowendel/django-rest-app/python-3-shield.svg)](https://pyup.io/repos/github/franciscowendel/django-rest-app/)
