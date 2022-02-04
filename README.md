### Create a virtual environment and activate it

https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/


### Then install all the libraries from requirements.txt
> pip install -r requirements.txt

### Open the folder 'backend' where there's the file 'manage.py' and run server:

> python manage.py runserver

# _________________

.
### // help
#### To delete all the data from database delete all the migrations and also database:
>  find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

> find . -path "*/migrations/*.pyc"  -delete
