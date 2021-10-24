

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
  * `{% include "name_snippet.html" with person="Jane" greeting="Hello" %}`


