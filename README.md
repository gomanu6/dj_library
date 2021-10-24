# dj_library
A library project for practicing Django

Starting Python 3.6 dictionaries are ordered.

### Steps to set up the project
#### Install Django

* install django for the venv with 
  * `python -m pip install django`
* verify django is installed
  * enter shell prompt by typing python
  * \>>>import django
  * \>>>print(django.get_version())
* or type `django-admin`
* Run `django-admin version` to display the current Django version.

### [django-admin and manage.py](https://docs.djangoproject.com/en/3.2/ref/django-admin/)
* Common Commands
  * check
  * runserver
  * makemigrations
  * migrate
  * showmigrations
  * shell
  * startapp
  * startproject
  * createsuperuser

#### Create Django Project

* \$ `django-admin startproject dj_lib`

#### Create an app (module)
* \$ `cd dj_lib`
* \$ `python manage.py startapp my_lib`
* \$ `python manage.py runserver`

#### VS Code 
* install Python extensions Python and Pylance
* Choose autoformater, install autopep8
* install Django extension, by Baptiste Darthenay
* Syntax highlighting for django html in vs code, settings.json
  * "emmet.includelanguages": { "django-html": "html" }

[Settings](https://docs.djangoproject.com/en/3.2/ref/settings/)

#### Create the Project structure /  urls / Routes
* Create a urls.py within the app (my_lib) folder
* `from django.urls import path`
* `from . import views`
* `urlpatterns = [
    path('', views.index, name='index')
]`
* create a dynamic url pattern, path converter / placeholder
  * `path('\<str:lib_book>/', views.book, name='book')`
  * `path('\<int:lib_book>/', views.book_number, name='book_number')`
  * `path('\<slug:lib_book>/', views.book_slug, name='book_slug')`
* link the urls.py for the app (my_lib) to the project by adding a path to the project (dj_lib) urls.py

### [Path Converters](https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters)
- str : Matches any non-empty string, excluding the path separator, '/'. This is the default if a converter isn’t included in the expression.
- int : Matches zero or any positive integer. Returns an int.
- slug : Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. For example, building-your-1st-django-site.
- uuid : Matches a formatted UUID. To prevent multiple URLs from mapping to the same page, dashes must be included and letters must be lowercase. For example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
- path : Matches any non-empty string, including the path separator, '/'. This allows you to match against a complete URL path rather than a segment of a URL path as with str.

- The string may contain angle brackets (like `<username>` this) to capture part of the URL and send it as a keyword argument to the view

### [django.urls functions for use in URLconfs](https://docs.djangoproject.com/en/3.2/ref/urls/)
- [path():](https://docs.djangoproject.com/en/3.2/ref/urls/#path) Returns an element for inclusion in urlpatterns. 
  - path(route, view, kwargs=None, name=None)
- [re_path():](https://docs.djangoproject.com/en/3.2/ref/urls/#re-path) Returns an element for inclusion in urlpatterns.
  - re_path(route, view, kwargs=None, name=None)
- [include():](https://docs.djangoproject.com/en/3.2/ref/urls/#include) A function that takes a full Python import path to another URLconf module that should be “included” in this place. Optionally, the application namespace and instance namespace where the entries will be included into can also be specified.
  - include(module, namespace=None)
  - include(pattern_list)
  - include((pattern_list, app_namespace), namespace=None)

### [django.conf.urls functions for use in URLconfs](https://docs.djangoproject.com/en/3.2/ref/urls/#module-django.conf.urls)
- [static():](https://docs.djangoproject.com/en/3.2/ref/urls/#static) Helper function to return a URL pattern for serving files in debug mode:
  - static.static(prefix, view=django.views.static.serve, **kwargs)
- [url():](https://docs.djangoproject.com/en/3.2/ref/urls/#url) This function is an alias to django.urls.re_path().
  - url(regex, view, kwargs=None, name=None)

### [django.http]()
- [HttpResponse](https://docs.djangoproject.com/en/3.2/ref/request-response/#django.http.HttpResponse)
- The HttpResponse class lives in the django.http module.
- To set or remove a header field in your response, use HttpResponse.headers
  - HttpResponse sub classes (from django.http import ..)
    - HttpResponseRedirect
    - HttpResponsePermanentRedirect
    - HttpResponseNotModified
    - HttpResponseBadRequest
    - HttpResponseNotFound : you are responsible for producing the html content that should go in there.
    - HttpResponseForbidden
    - HttpResponseNotAllowed
    - HttpResponseGone
    - HttpResponseServerError
    - JsonResponse : An HttpResponse subclass that helps to create a JSON-encoded response.
  - StreamingHttpResponse : The StreamingHttpResponse class is used to stream a response from Django to the browser. You might want to do this if generating the response takes too long or uses too much memory. For instance, it’s useful for generating large CSV files.
    - Django is designed for short-lived requests. Streaming responses will tie a worker process for the entire duration of the response. This may result in poor performance. Generally speaking, you should perform expensive tasks outside of the request-response cycle, rather than resorting to a streamed response.
    - The StreamingHttpResponse is not a subclass of HttpResponse, because it features a slightly different API.
    - should only be used in situations where it is absolutely required that the whole content isn’t iterated before transferring the data to the client. Because the content can’t be accessed, many middleware can’t function normally. For example the ETag and Content-Length headers can’t be generated for streaming responses.
      - FileResponse : FileResponse is a subclass of StreamingHttpResponse optimized for binary files. It uses wsgi.file_wrapper if provided by the wsgi server, otherwise it streams the file out in small chunks.





#### url resolvers / Build dynamic urls

### [django.urls utility functions :](https://docs.djangoproject.com/en/3.2/ref/urlresolvers/#module-django.urls)
* reverse() - to use in views/code to refer or redirect
  * `from django.urls import reverse`
  * `reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)`
  * If the URL accepts arguments, you may pass them in args or kwargs.
* Tag: url() - use in templates for links
  * url(regex, view, kwargs=None, name=None)



### [Static Files App](https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#module-django.contrib.staticfiles)
- django.contrib.staticfiles collects static files from each of your applications (and any other places you specify) into a single location that can easily be served in production.
- [Managing static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/3.2/howto/static-files/)
- [Deploying Static Files](https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/)


#### 404 Page
* import Http404 from django.http
* django looks for a 404.html file in the common templates folder by default (dj_library/dj_lib/templates) 
* raise an error
  * `raise Http404()`
  * can pass an error message to that
  * during development, 404 page is not displayed

#### Static files (css/js/etc)
* similar structure as the templates folder
* project_folder/project_name/app_folder/static/app_name/static_file
* settings.py
  * INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
]
  * STATIC_URL = '/static/' ==> tells django under which url to serve static assets, and hence not related to loading static files in the template
  * Django automatically detects static folder in app folders
  * Tag: {% load static %} ==> in the template to add the link url for the file
  * Base Template
    * {% block css_files %}
    * 
    * {% endblock %}
  * Page Template
    * `{% load static %}`
    * `{% block css_files %}`
    * `<link rel="stylesheet" href="{% static 'my_lib/subject.css' %}">`
    * `{% endblock %}`
  * Static Files in the common folders
    * Django does not look in the main folder for a static folder
      * Add in settings.py
        * STATICFILES_DIRS = [
      BASE_DIR / "static"
]
      * Base.html
        * `{% load static %}`
        * ....
        * `<link rel="stylesheet" href="{% static 'base.css' %}" >`


### [Some of the Commands provided by applications](https://docs.djangoproject.com/en/3.2/ref/django-admin/#commands-provided-by-applications)
- [createsuperuser](https://docs.djangoproject.com/en/3.2/ref/django-admin/#createsuperuser)
  - `python manage.py createsuperuser`
  - Register models in admin.py
  - This command is only available if Django’s authentication system (django.contrib.auth) is installed.
  - This is useful if you need to create an initial superuser account or if you need to programmatically generate superuser accounts for your site(s).
- [changepassword](https://docs.djangoproject.com/en/3.2/ref/django-admin/#changepassword)
  - This command is only available if Django’s authentication system (django.contrib.auth) is installed.
  - If you do not supply a user, the command will attempt to change the password whose username matches the current user.
- clearsessions
  - `django-admin clearsessions`
  - `django.contrib.sessions`
  - Can be run as a cron job or directly to clean out expired sessions.
- [collectstatic](https://docs.djangoproject.com/en/3.2/ref/django-admin/#collectstatic)
  - This command is only available if the static files application (django.contrib.staticfiles) is installed.
  - [description](https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#collectstatic)
  - Collects the static files into STATIC_ROOT.
- [findstatic](https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#findstatic)
  - django-admin findstatic staticfile \[staticfile ...]
  - Searches for one or more relative paths with the enabled finders.
  - This is a debugging aid; it’ll show you exactly which static file will be collected for a given path.
  - 

### [Admin Area](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#module-django.contrib.admin)
- Register models in admin.py
  - `from django.contrib import admin`
  - `from .models import Book`
  - `admin.site.register(Book)`
- To edit functionality in the admin.py
  - Add a class to modify the functionality
  - `class BookAdmin(admin.ModelAdmin)`
    - `readonly_fields = ("slug")` 
    - `prepopulated_fields = {"slug": ("title",)}` # does not work with readonly_fields attribute
  - `list_filter = ("author", "rating")` # add filter functionality
  - list_display = ("title", "author") # change the fields displayed in teh admin table



### Deployment
- Check settings
- Collect Static Files
- migrate database
- freeze requirements
  - create virtual env
  - install required packages
  - python -m pip freeze > requirements.txt
- Environment variables
  - ALLOWED_HOSTS = [ domain_where_it_is_hosted]
  - `from os import getenv`
  - ALLOWED_HOSTS = [ getevn("APP_HOST)]
  - SECRET_KEY = getenv("SECRET_KEY")
  - DEBUG = getenv("IS_DEVELOPMENT", True)
- Elastic Beanstalk
  - create folder .ebextensions
  - django.config
    - `option_settings:`
      - `aws:elasticbeanstalk:container:python:`
        - `WSGIPATH: my_site.wsgi:application`
  - configure SSL and custom domain
  - migrate to postgres
  - let nginx serve static files
    - static-files.config
    - `option_settings:`
      - `aws:elasticbeanstalk:environment:proxy:staticfiles:`
        - `/static: staticfiles`
        - `/files: uploads`