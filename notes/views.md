

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



