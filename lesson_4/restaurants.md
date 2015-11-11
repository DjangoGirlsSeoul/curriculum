Making a simple restaurants review app
---

Requirements: 
- Python 3+ and Django 1.8+ installed

1. Make a new folder 
2. Create a new virtualenv and activate it
3. `pip install django`
4. `django-admin startproject restaurants`
5. `django-admin startapp best`
6. Make a list of restaurants with its features in a dictionary
7. Create a template in `best/templates/best/index.py`
8. Create a `urls.py` for `best` app
9. Link `best` `urls.py` with `restaurants` `urls.py`
10. `python manage.py runserver`
11. Go to `localhost:8000/best`
