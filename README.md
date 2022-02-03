To run server, if you don't use linux, create virtual environment and:

> pip install -r requirements.txt

else:

> . me/bin/activate


To run server:

> python3 manage.py runserver


To delete all migrations:

> find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
>
> find . -path "*/migrations/*.pyc"  -delete
