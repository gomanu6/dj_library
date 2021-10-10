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


#### Views
* *View is a function or logic that should execute when a supported url is reached*
* Each view is responsible for returning an HttpResponse object.
* Each view you write is responsible for instantiating, populating, and returning an HttpResponse.
* use HttpResponse and HttpResponseNotFound to return data
* use HttpResponseRedirect to redirect to the correct url
* [render_to_string() :](https://docs.djangoproject.com/en/3.2/topics/templates/#django.template.loader.render_to_string) render the template to string and return with HttpResponse.
  * `render_to_string(template_name, context=None, request=None, using=None)`
  * `from django.template.loader import render_to_string`
* render() - default way to use templates, shortcut for render_to_string(), always sends the success response
  * `from django.shortcuts import render`
  * render(request, template_name, context=None, content_type=None, status=None, using=None)
    * request is required
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



### Templating
- [Django Templating Language](https://docs.djangoproject.com/en/3.2/topics/templates/#the-django-template-language)
- [Django template Language](https://docs.djangoproject.com/en/3.2/ref/templates/language/#the-django-template-language)
- [The Django template language: for Python programmers](https://docs.djangoproject.com/en/3.2/ref/templates/api/#the-django-template-language-for-python-programmers)
  - A Django template is a text document or a Python string marked-up using the Django template language. Some constructs are recognized and interpreted by the template engine. The main ones are variables and tags.
  - A template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags. Everything else is output as is.
  - The syntax of the Django template language involves four constructs.
    - **Variables**
      - Variables are surrounded by {{ and }}.
      - `My first name is {{ first_name }}. My last name is {{ last_name }}.`
      - Context is a dict-like object mapping keys to values.
      - `{'first_name': 'John', 'last_name': 'Doe'}`
      - If a variable resolves to a callable, the template system will call it with no arguments and use its result instead of the callable.
    - **Tags**
      - Tags are surrounded by {% and %}.
      - [Common Built-in Tags reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-tag-reference)
        - block : `{% block %} {% endblock %}`
        - add : 
        - comment : `{% comment %} and {% endcomment %}`
        - {% csrf_token %}
        - extends : Signals that this template extends a parent template.
          - This tag can be used in two ways:
            - {% extends "base.html" %} (with quotes) uses the literal value "base.html" as the name of the parent template to extend.
            - {% extends variable %} uses the value of variable. If the variable evaluates to a string, Django will use that string as the name of the parent template. If the variable evaluates to a Template object, Django will use that object as the parent template.
        - for : {% for ... %} {% endfor %}
        - if : {% if ... %} {% endif %}
        - include : Loads a template and renders it with the current context. This is a way of “including” other templates within a template.
          - `{% include "foo/bar.html" %}`
        - load : Loads a custom template tag set.
          - `{% load somelibrary package.otherlibrary %}`
        - lorem : `{% lorem [count] [method] [random] %}`
        - now : Displays the current date and/or time, using a format according to the given string.
        - url : Returns an absolute path reference (a URL without the domain name) matching a given view and optional parameters.
          - `{% url 'some-url-name' v1 v2 %}`
          - `{% url 'some-url-name' arg1=v1 arg2=v2 %}`
    - **Filters**
      - {{ django|title }} for  context `{'django': 'the web framework for perfectionists with deadlines'}`
      - Some filters take an argument: `{{ my_date|date:"Y-m-d" }}`
      - [Built-In Filters:](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-filter-reference)
        - Common filters
          - title
          - capfirst
          - date
          - dictsort - 
          - first - returns the first item in a list.
          - last
          - join - Joins a list with a string, like Python’s str.join(list)
          - length - works with strings and lists
          - lower
          - upper
          - random
          - slice
          - slugify
          - time
    - [Other Tags and Filters libraries](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#other-tags-and-filters-libraries)
      - static : To link to static files that are saved in [STATIC_ROOT](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-STATIC_ROOT)
        - `{% load static %} <img src="{% static 'images/hi.jpg' %}" alt="Hi!">`
      - STATIC_ROOT : The absolute path to the directory where collectstatic will collect static files for deployment.
      - STATIC_URL : URL to use when referring to static files located in STATIC_ROOT.
      - STATICFILES_DIRS : This setting defines the additional locations the staticfiles app will traverse if the FileSystemFinder finder is enabled, e.g. if you use the collectstatic or findstatic management command or use the static file serving view.
        - `STATICFILES_DIRS = [
    "/home/special.polls.com/polls/static",
    "/home/polls.com/polls/static",
    "/opt/webfiles/common",
]`
      - STATICFILES_STORAGE : The file storage engine to use when collecting static files with the collectstatic management command.
      - STATICFILES_FINDERS : The list of finder backends that know how to find static files in various locations.
    - **Comments**
      - `{# this won't be rendered #}`
      - A {% comment %} tag provides multi-line comments.
    - [Custom Template Tags and Filters](https://docs.djangoproject.com/en/3.2/howto/custom-template-tags)

### [Static Files App](https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#module-django.contrib.staticfiles)
- django.contrib.staticfiles collects static files from each of your applications (and any other places you specify) into a single location that can easily be served in production.
- [Managing static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/3.2/howto/static-files/)
- [Deploying Static Files](https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/)


#### Create templates
* link the template directory for the app into the project settings file
* Django by default looks for templates folders inside the app folders.
* Register the app in the setings.py folder so that the template folder is used by Django. 
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
  * project_folder/main_project/app_name/templates/app_name/template_name.html
  * my_lib/templates/my_lib/index.html


#### Interpolation
- can be used throughout the Html document.

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
* TEMPLATES = {
* ......
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
* Tag: [include](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#include)
  * Loads a template and renders it with the current context. This is a way of “including” other templates within a template.
  * The template name can either be a variable or a hard-coded (quoted) string, in either single or double quotes.
  * {% include "foo/bar.html" %}
  * {% include "name_snippet.html" with person="Jane" greeting="Hello" %}
  * path to the partial file can be absolute or relative from the template file
  * included partials have access to the variables / contexts from the views
  * Can pass additional variables or data into partials with the `with` option
  * `{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
`


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

### Models
* https://docs.djangoproject.com/en/3.2/ref/models/fields/
* Shell
* validators




