# dj_library
A library project for practicing Django

### Steps to set up the project
####Install Django

* install django for the venv with 
  * python -m pip install django
* verify django is installed
  * enter shell prompt by typing python
  * \>>>import django
  * \>>>print(django.get_version())
* or type django-admin

#### Create Django Project

* \$ django-admin startproject dj_lib

#### Create an app
* \$ cd dj_lib
* \$ python manage.py startapp my_lib
* \$ python manage.py runserver

#### Create the Project structure
* Create a urls.py within the app folder
* from django.urls import path
* from . import views
* urlpatterns = [
    path('', views.index, name='index')
]

