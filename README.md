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
* [Class based views](https://docs.djangoproject.com/en/3.2/topics/class-based-views/)
  * 




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

### [Models](https://docs.djangoproject.com/en/3.2/ref/models/)
- A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
- Each model is a Python class that subclasses django.db.models.Model.
- Each attribute of the model represents a database field.
- Each field is specified as a class attribute, and each attribute maps to a database column.
* Field Types
  * Each field in your model should be an instance of the appropriate Field class. 
  * Django uses the field class types to determine a few things:
    * The column type, which tells the database what kind of data to store (e.g. INTEGER, VARCHAR, TEXT).
    * The default HTML widget to use when rendering a form field (e.g. `<input type="text">`, `<select>`).
    * The minimal validation requirements, used in Django’s admin and in automatically-generated forms.
  * [Common Field Types](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types)
    * BooleanField : True or False. The default value of BooleanField is None when Field.default isn’t defined.
    * CharField : A string field, for small- to large-sized strings.
      * `class CharField(max_length=None, **options)`
      * Required argument: CharField.max_length - The maximum length (in characters) of the field. The max_length is enforced at the database level and in Django’s validation using MaxLengthValidator.
    * DateField : A date, represented in Python by a datetime.date instance. Has a few extra, optional arguments:
      * `class DateField(auto_now=False, auto_now_add=False, **options)`
    * DateTimeField : A date and time, represented in Python by a datetime.datetime instance. Takes the same extra arguments as DateField.
      * `class DateTimeField(auto_now=False, auto_now_add=False, **options)`
    * EmailField : A CharField that checks that the value is a valid email address using EmailValidator.
      * `class EmailField(max_length=254, **options)`
    * FileField : 
      * `class FileField(upload_to=None, max_length=100, **options)`
    * ImageField : Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
      * `class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)`
      * Requires the [Pillow](https://pillow.readthedocs.io/en/latest/) library.
    * IntegerField : It uses MinValueValidator and MaxValueValidator to validate the input based on the values that the default database supports.
    * FloatField : A floating-point number represented in Python by a float instance.
    * JSONField : 
      * `class JSONField(encoder=None, decoder=None, **options)`
    * SlugField : If max_length is not specified, Django will use a default length of 50.
      * It is often useful to automatically prepopulate a SlugField based on the value of some other value. You can do this automatically in the admin using [prepopulated_fields](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields).
      * `class SlugField(max_length=50, **options)`
    * TextField : A large text field. The default form widget for this field is a Textarea.
    * TimeField : A time, represented in Python by a datetime.time instance. Accepts the same auto-population options as DateField.
      * `class TimeField(auto_now=False, auto_now_add=False, **options)`
    * URLField : A CharField for a URL, validated by URLValidator.
      * `class URLField(max_length=200, **options)`
      * If you don’t specify max_length, a default of 200 is used.
* [Relationship Fields](https://docs.djangoproject.com/en/3.2/ref/models/fields/#module-django.db.models.fields.related)
  * ForeignKey : A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.
    * `class ForeignKey(to, on_delete, **options)`
    * on_delete : 
      * CASCADE : Cascade deletes. Django emulates the behavior of the SQL constraint ON DELETE CASCADE and also deletes the object containing the ForeignKey.
      * PROTECT : Prevent deletion of the referenced object by raising ProtectedError, a subclass of django.db.IntegrityError.
      * RESTRICT : Prevent deletion of the referenced object by raising RestrictedError (a subclass of django.db.IntegrityError).
      * SET_NULL : Set the ForeignKey null; this is only possible if null is True.
      * SET_DEFAULT : Set the ForeignKey to its default value; a default for the ForeignKey must be set.
      * SET() : Set the ForeignKey to the value passed to SET(), or if a callable is passed in, the result of calling it. In most cases, passing a callable will be necessary to avoid executing queries at the time your models.py is imported:
      * DO_NOTHING : Take no action. If your database backend enforces referential integrity, this will cause an IntegrityError unless you manually add an SQL ON DELETE constraint to the database field.
    * related_name : 
      * The name to use for the relation from the related object back to this one. It’s also the default value for related_query_name (the name to use for the reverse filter name from the target model)
    * related_query_name :
      * The name to use for the reverse filter name from the target model. It defaults to the value of related_name or default_related_name if set, otherwise it defaults to the name of the model:
    * limit_choices_to
  * ManyToManyField : A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships.
    * `class ManyToManyField(to, **options)`
    * Some Arguments (optional)
      * related_name
      * related_query_name
      * limit_choices_to
      * symmetrical
      * through
      * through_fields
  * OneToOneField : A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the “reverse” side of the relation will directly return a single object.
    * This is most useful as the primary key of a model which “extends” another model in some way; Multi-table inheritance is implemented by adding an implicit one-to-one relation from the child model to the parent model, for example.
    * `class OneToOneField(to, on_delete, parent_link=False, **options)`
    * If you do not specify the related_name argument for the OneToOneField, Django will use the lowercase name of the current model as default value.
    * Additionally, OneToOneField accepts all of the extra arguments accepted by ForeignKey, plus one extra argument:
      * parent_link : When True and used in a model which inherits from another concrete model, indicates that this field should be used as the link back to the parent class, rather than the extra OneToOneField which would normally be implicitly created by subclassing.
* [Class Meta](https://docs.djangoproject.com/en/3.2/topics/db/models/#meta-options) : Model metadata is “anything that’s not a field”, such as ordering options (ordering), database table name (db_table), or human-readable singular and plural names (verbose_name and verbose_name_plural). None are required, and adding class Meta to a model is completely optional.
  * [Common Model Meta Options](https://docs.djangoproject.com/en/3.2/ref/models/options/)
    * app_label : If a model is defined outside of an application in INSTALLED_APPS, it must declare which app it belongs to:
    * default_related_name : The name that will be used by default for the relation from a related object back to this one. The default is <model_name>_set.
    * ordering : The default ordering for the object, for use when obtaining lists of objects:
    * permissions : Extra permissions to enter into the permissions table when creating this object. Add, change, delete, and view permissions are automatically created for each model. This example specifies an extra permission, can_deliver_pizzas:
  * Read Only Meta Attributes
    * label : Representation of the object, returns app_label.object_name, e.g. 'polls.Question'.
    * label_lower : Representation of the model, returns app_label.model_name, e.g. 'polls.question'.
* [Model Methods](https://docs.djangoproject.com/en/3.2/topics/db/models/#model-methods)
  * [methods with special purposes](https://docs.djangoproject.com/en/3.2/ref/models/instances/#other-model-instance-methods)
    * __str__()
      * The __str__() method is called whenever you call str() on an object. Django uses str(obj) in a number of places. Most notably, to display an object in the Django admin site and as the value inserted into a template when it displays an object. Thus, you should always return a nice, human-readable representation of the model from the __str__() method.
      * `def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)`
    * __eq__()
      * The equality method is defined such that instances with the same primary key value and the same concrete class are considered equal, except that instances with a primary key value of None aren’t equal to anything except themselves. For proxy models, concrete class is defined as the model’s first non-proxy parent; for all other models it’s simply the model’s class.
    * __hash__()
      * The __hash__() method is based on the instance’s primary key value. It is effectively hash(obj.pk). If the instance doesn’t have a primary key value then a TypeError will be raised (otherwise the __hash__() method would return different values before and after the instance is saved, but changing the __hash__() value of an instance is forbidden in Python.
    * get_absolute_url()
      * Define a get_absolute_url() method to tell Django how to calculate the canonical URL for an object. To callers, this method should appear to return a string that can be used to refer to the object over HTTP.
      * `def get_absolute_url(self):
    from django.urls import reverse
    return reverse('people-detail', kwargs={'pk' : self.pk})`
    * save()
      * `Model.save(force_insert=False, force_update=False, using=DEFAULT_DB_ALIAS, update_fields=None)`
      * [What happens when you save?](https://docs.djangoproject.com/en/3.2/ref/models/instances/#what-happens-when-you-save)
    * [delete](https://docs.djangoproject.com/en/3.2/ref/models/instances/#deleting-objects)
      * The delete method, conveniently, is named delete(). This method immediately deletes the object and returns the number of objects deleted and a dictionary with the number of deletions per object type. Example:
        * `Model.delete(using=DEFAULT_DB_ALIAS, keep_parents=False)`
    * [Queryset](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#queryset-api)
      * `class QuerySet(model=None, query=None, using=None, hints=None)`
      * [Some Methods that return new QuerySets](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#methods-that-return-new-querysets)
        * filter()
        * exclude()
        * annotate()
        * alias()
        * values()
        * dates()
        * reverse()
      * [Operators that return new QuerySets](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#operators-that-return-new-querysets)
        * AND
        * OR
      * [Some Methods that do not return QuerySets](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#methods-that-do-not-return-querysets)
        * get()
        * create()
        * get_or_create()
        * update_or_create()
        * count()
        * iterator()
        * latest()
        * earliest()
        * first()
        * last()
        * delete()
        * update()
        * exists()
    * [Field Lookups](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups)
      * exact : exact match, iexact : case insensitive exact match
      * contains, icontains
      * lt, gt, lte, gte
        * `Entry.objects.filter(pub_date__lte='2006-01-01')`
      * startswith, istartswith
      * endswith, iendswith
      * regex, iregex
    * [Complex lookups with Q objects](https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects)
      * `from django.db.models import Q`
      * `Q(question__startswith='Who') | Q(question__startswith='What')`
      * Also, Q objects can be negated using the ~ operator, allowing for combined lookups that combine both a normal query and a negated (NOT) query:
      * `Q(question__startswith='Who') | ~Q(pub_date__year=2005)`
    * Performance in queries
      * Django reaches out to the database once we do something with the result of the query.
      * If we query the database and use the result, tt also caches the result of queries and uses the cached results if we chain any further queries with the previous queries.
      * 
* Shell
  * `from mylib.models import Book`
  * Book.objects.all() => gets all the objects in the Book Table
  * hp = Book(title="..."...) => creates a new Book object
  * hp.save() => saves the new book object
  * Book.objects.create(title="...."....) = Creates and saves a new book in the database
* validators
* [Common optional Field options available for Field Types](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options)
  * null : If True, Django will store empty values as NULL in the database. Default is False.
  * blank : If True, the field is allowed to be blank. Default is False.
  * default : The default value for the field.
  * editable : If False, the field will not be displayed in the admin or any other ModelForm. They are also skipped during model validation. Default is True.
  * primary_key : If you don’t specify primary_key=True for any field in your model, Django will automatically add a field to hold the primary key, so you don’t need to set primary_key=True on any of your fields unless you want to override the default primary-key behavior.
  * error_messages : The error_messages argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override.
  * unique : This is enforced at the database level and by model validation. If you try to save a model with a duplicate value in a unique field, a django.db.IntegrityError will be raised by the model’s save() method.
* Attributes for fields
  * auto_created : Boolean flag that indicates if the field was automatically created, such as the OneToOneField used by model inheritance.
  * concrete : Boolean flag that indicates if the field has a database column associated with it.
  * hidden : Boolean flag that indicates if a field is used to back another non-hidden field’s functionality (e.g. the content_type and object_id fields that make up a GenericForeignKey). The hidden flag is used to distinguish what constitutes the public subset of fields on the model from all the fields on the model.
  * is_relation : Boolean flag that indicates if a field contains references to one or more other models for its functionality (e.g. ForeignKey, ManyToManyField, OneToOneField, etc.).
  * model : Returns the model on which the field is defined. If a field is defined on a superclass of a model, model will refer to the superclass, not the class of the instance.
* Attributes for fields with relations
  * many_to_many : Boolean flag that is True if the field has a many-to-many relation; False otherwise. The only field included with Django where this is True is ManyToManyField.
  * many_to_one : Boolean flag that is True if the field has a many-to-one relation, such as a ForeignKey; False otherwise.
  * one_to_many : Boolean flag that is True if the field has a one-to-many relation, such as a GenericRelation or the reverse of a ForeignKey; False otherwise.
  * one_to_one : Boolean flag that is True if the field has a one-to-one relation, such as a OneToOneField; False otherwise.
  * related_model : Points to the model the field relates to. For example, Author in ForeignKey(Author, on_delete=models.CASCADE). The related_model for a GenericForeignKey is always None.
* [Querying Data from the Database](https://docs.djangoproject.com/en/3.2/topics/db/queries/)
  * Book.objects.get(id=3)
  * Book.objects.get(title="...")
  * get() => gets a single data even if it matches more
  * Book.objects.filter() => can return multiple objects
  * Book.objects.filter(is_bestselling=True)
  * Book.objects.filter(is_bestselling=True, rating=5)
  * Book.objects.filter(rating__lte=3)


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