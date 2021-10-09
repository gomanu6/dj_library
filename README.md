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

- The string may contain angle brackets (like <username> above) to capture part of the URL and send it as a keyword argument to the view

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
  - HttpResponse sub classes
    - HttpResponseRedirect
    - HttpResponsePermanentRedirect
    - HttpResponseNotModified
    - HttpResponseBadRequest
    - HttpResponseNotFound
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


#### Views
* *View is a function or logic that should execute when a supported url is reached*
* Each view is responsible for returning an HttpResponse object.
* Each view you write is responsible for instantiating, populating, and returning an HttpResponse.
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

### [django.urls utility functions :](https://docs.djangoproject.com/en/3.2/ref/urlresolvers/#module-django.urls)
* reverse() - to use in views/code to refer or redirect
  * `from django.urls import reverse`
  * `reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)`
  * If the URL accepts arguments, you may pass them in args or kwargs.
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




