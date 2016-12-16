Create a virtual environment:
-----------------------------

```python
cd ~/path/to/progressive-giving/
virtualenv venv
source venv/bin/activate
```

To run locally:
---------------

```python
cd ~/path/to/progressive-giving/
source venv/bin/activate
pip install -r requirements.txt
cd giving
python manage.py migrate
python manage.py runserver
```

To create a superuser (for admin access):
-----------------------------------------

```python
cd ~/path/to/progressive-giving/
python manage.py createsuperuser
```

To view the admin:
------------------

http://127.0.0.1:8000/admin/
