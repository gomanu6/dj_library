# dj_library
A library project for practicing Django

### Steps to set up the project
#### Install Django

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

#### VS Code 
* install Python extention
* Install Pylance
* Choose autoformater, install autopep8
* install Django extension, by Baptiste Darthenay
* Syntax highlighting for django html in vs code, settings.json
  * "emmet.includelanguages": { "django-html": "html" }

#### Create the Project structure /  urls / Routes
* Create a urls.py within the app folder
* from django.urls import path
* from . import views
* urlpatterns = [
    path('', views.index, name='index')
]
* create a dynamic url pattern, path converter
  * path('\<str:lib_book>/', views.book, name='book'
* link the urls.py for the app to the project by adding a path to the project urls.py

#### Views
* use HttpResponse and Http ResponseNotFound to return data
* use HttpResponseRedirect to redirect to the correct url
* render_to_string()
  * render_to_string(template_name, context=None, request=None, using=None)
  * https://docs.djangoproject.com/en/3.2/topics/templates/#django.template.loader.render_to_string
  * from django.template.loader import render_to_string
* render() - default way to use templates
  * from django.shortcuts import render
  * render(request, template_name, context=None, content_type=None, status=None, using=None)
  * template_name = 'my_lib/subject.html'
  * context = dict, used to pass values to the template




#### url resolvers / Build dynamic urls
* reverse() - to use in views to refer or redirect
  * from django.urls import reverse
  * reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)
* Tag: url() - use in templates for links
  * url(regex, view, kwargs=None, name=None)




#### Create templates
* link the template directory for the app into the project settings file
  * INSTALLED_APPS = [
    'my_lib',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
  * OR
  * TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "app_name" / "templates"],
  * and link the rest of the url in the view where it is required
    * 
* Template hierarchy
  * app_name/templates/app_name/template_name.html
  * my_lib/templates/my_lib/index.html


#### Interpolation

##### Tags
* https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-tag-reference
* Tag: url - construct a url for a link inside a template
  * {% url 'some-url-name' v1 v2 %}
  * {% url 'some-url-name' arg1=v1 arg2=v2 %}
* Tag: for - for loops inside templates
  * {% for subject in subjects %}
  * \<li>\<a href="{% url 'subject' subject %}">{{subject|title }}\</a>\</li>
  * {% endfor %}
* Tag: if - if logic inside a template
  * {% if condition %}
  * statement
  * {% elif condition %}
  * statement
  * {% else %}
  * statement
  * {% endif %}

##### Filters
* https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-filter-reference


#### Template inheritance
* Base template in common templates folder under the main project folder
* dj_lib/templates/base.html
* 'DIRS': [ BASE_DIR / "templates" ],
* Tag: block
  * Create Block in the base template
    * {% block block_name %}
    * .....data....
    * {% endblock %}
  * Extend block in specific template
    * {% extends "base.html" %}
    * {% block title %}My amazing blog{% endblock %}

#### Includes / Partials
* Tag: include
  * https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#include
  * Loads a template and renders it with the current context. This is a way of “including” other templates within a template.
  * The template name can either be a variable or a hard-coded (quoted) string, in either single or double quotes.
  * {% include "foo/bar.html" %}
  * {% include "name_snippet.html" with person="Jane" greeting="Hello" %}
  * path to the partial file can be relative or absolute from the template file
  * included partials have access to the variables / contexts from the views


#### 404 Page
* import Http404 from django.http
* django looks for a 404.html file in the common templates folder by default (my_lib/templates) 
* raise an error
  * raise Http404()
  * during development, 404 page is not displayed

#### Static files (css/js/etc)
* similar structure as the templates folder
* app_folder/static/app_name/static_file
* settings.py
  * INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
]
  * STATIC_URL = '/static/' ==> tells django under which url to serve static assets, and hence not related to loading static files in the template
  * Django automatically detects static folder in app folders
  * Tag: {% load static %}
  * Base Template
    * {% block css_files %}
    * 
    * {% endblock %}
  * Page Template
    * {% load static %}
    * {% block css_files %}
    * <link rel="stylesheet" href="{% static 'my_lib/subject.css' %}" >
    * {% endblock %}
  * Static Files in the common folders
    * Add in settings.py
      * STATICFILES_DIRS = [
    BASE_DIR / "static"
]
    * Base.html
      * {% load static %}
      * ....
      * \<link rel="stylesheet" href="{% static 'base.css' %}" >

### Models
* https://docs.djangoproject.com/en/3.2/ref/models/fields/
* Shell
* validators
* 