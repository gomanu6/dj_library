
### Forms


### CSRF Token
- {% csrf_token %}
- keep the tag inside the form

### GET or POST
- Any request that could be used to change the state of the system - for example, a request that makes changes in the database - should use POST. 
- GET should be used only for requests that do not affect the state of the system.
- GET is suitable for things like a web search form, because the URLs that represent a GET request can easily be bookmarked, shared, or resubmitted.
- action = path after the domain to which the request should be sent
- action ="/" = 
- request object has a method property
- request.method = GET or POST
- request.POST holds a dictionary where the keys are the name of the input tags and values are the entered values
- `<input type="text" name="username" >`
- `request.POST['username']` will return the entered value
- Best Practice is to redirect to a new url with a get request after submitting a post form
- in the POST request view you can check the validity of the entered input and return a context with keys for errors to display in the template

### [Form Class](https://docs.djangoproject.com/en/3.2/topics/forms/#the-django-form-class)
- In a similar way that a model class’s fields map to database fields, a form class’s fields map to HTML form <input> elements.
- ModelForm maps a model class’s fields to HTML form <input> elements via a Form; this is what the Django admin is based upon.)

### [Form Fields](https://docs.djangoproject.com/en/3.2/ref/forms/fields/)
- [Field Classes](https://docs.djangoproject.com/en/3.2/ref/forms/fields/#built-in-field-classes)
  - BooleanField
    - Default widget: CheckboxInput
    - Normalizes to: A Python True or False value.
    - Error message keys: required
    - Since all Field subclasses have required=True by default, the validation condition here is important. If you want to include a boolean in your form that can be either True or False (e.g. a checked or unchecked checkbox), you must remember to pass in required=False when creating the BooleanField.
  - CharField
    - Default widget: TextInput
    - Normalizes to: A string.
    - Error message keys: required, max_length, min_length
    - Has four optional arguments for validation
      - max_length
      - min_length
      - strip : If True (default), the value will be stripped of leading and trailing whitespace.
      - empty_value : The value to use to represent “empty”. Defaults to an empty string.
  - ChoiceField
    - Default widget: Select
    - Normalizes to: A string.
    - Error message keys: required, invalid_choice
    - Takes one extra argument
      - choices
        - Either an iterable of 2-tuples to use as choices for this field, enumeration choices, or a callable that returns such an iterable. This argument accepts the same formats as the choices argument to a model field. See the model field reference documentation on choices for more details. If the argument is a callable, it is evaluated each time the field’s form is initialized, in addition to during rendering. Defaults to an empty list.
  - DateField
    - Default widget: DateInput
    - Normalizes to: A Python datetime.date object.
    - Error message keys: required, invalid
    - Takes one optional argument
      - input_formats
        - A list of formats used to attempt to convert a string to a valid datetime.date object.
  - DateTimeField
    - Default widget: DateTimeInput
    - Normalizes to: A Python datetime.datetime object.
    - Error message keys: required, invalid
    - Takes one optional argument:
      - input_formats
        - A list of formats used to attempt to convert a string to a valid datetime.datetime object, in addition to ISO 8601 formats
  - DecimalField
  - DurationField
  - EmailField
  - FileField
  - FilePathField
  - ImageField
    - Using an ImageField requires that Pillow is installed with support for the image formats you use. If you encounter a corrupt image error when you upload an image, it usually means that Pillow doesn’t understand its format. To fix this, install the appropriate library and reinstall Pillow.
    - When you use an ImageField on a form, you must also remember to bind the file data to the form
  - IntegerField
  - JSONField
    - Default widget: Textarea
    - Normalizes to: A Python representation of the JSON value (usually as a dict, list, or None), depending on JSONField.decoder.
    - Takes two optional arguments
      - encoder
        - A json.JSONEncoder subclass to serialize data types not supported by the standard JSON serializer (e.g. datetime.datetime or UUID). For example, you can use the DjangoJSONEncoder class. 
        - Defaults to json.JSONEncoder.
      - decoder
        - A json.JSONDecoder subclass to deserialize the input. Your deserialization may need to account for the fact that you can’t be certain of the input type. For example, you run the risk of returning a datetime that was actually a string that just happened to be in the same format chosen for datetimes.
        - Defaults to json.JSONDecoder.
      - If you use a ModelForm, the encoder and decoder from JSONField will be used.
      - JSONField is not particularly user friendly in most cases. However, it is a useful way to format data from a client-side widget for submission to the server.
  - GenericIPAddressField
  - MultipleChoiceField
  - RegexField
  - SlugField
  - TimeField
  - URLField
- [Core field arguments](https://docs.djangoproject.com/en/3.2/ref/forms/fields/#core-field-arguments)
  - required : By default, each Field class assumes the value is required, so if you pass an empty value – either None or the empty string ("") – then clean() will raise a ValidationError exception
  - label : The label argument lets you specify the “human-friendly” label for this field. This is used when the Field is displayed in a Form.
    - the default label for a Field is generated from the field name by converting all underscores to spaces and upper-casing the first letter
  - label_suffix : The label_suffix argument lets you override the form’s label_suffix on a per-field basis:
  - initial : The initial argument lets you specify the initial value to use when rendering this Field in an unbound Form.
    - To specify dynamic initial data, see the [Form.initial](https://docs.djangoproject.com/en/3.2/ref/forms/api/#django.forms.Form.initial) parameter.
  - widget : The widget argument lets you specify a Widget class to use when rendering this Field. See Widgets for more information.
  - help_text : If you provide help_text, it will be displayed next to the Field when the Field is rendered by one of the convenience Form methods (e.g., as_ul()).
  - error_messages : The error_messages argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override. For example, here is the default error message:
    - `name = forms.CharField(error_messages={'required': 'Please enter your name'})`
  - validators : The validators argument lets you provide a list of validation functions for this field.
  - disabled : The disabled boolean argument, when set to True, disables a form field using the disabled HTML attribute so that it won’t be editable by users. Even if a user tampers with the field’s value submitted to the server, it will be ignored in favor of the value from the form’s initial data.
  - localize : The localize argument enables the localization of form data input, as well as the rendered output.
