

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
      * slug = models.SlugField()
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
    * ManytoMany relationshios between tables creates a mapping table that maps the relationships
    * add method
      * `germany = Country(name="Germany", code="DE")`
      * `mys = Book.objects.all()[0]`
      * `mys.published_countries.add(germany)`
      * `mys.published_countries.get(...)`
      * name of relation between Country and Book
        * `class Book(models.Model):`
        * .....
        * `published_countries = models.ManyToManyField(Country)`
        * From Country perspective
          * `ger = Country.objects.all()[0]`
          * `ger.book_set.all()`
          * book_set = objects
          * book_set = class name (Book) in lowercase + _set
        * From Book perspective
          * bk = Book.objects.get(title=(...))
          * bk.published_countries # returns the list of countries
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
    * verbose_name_plural : The plural name for the object, `verbose_name_plural = "stories"`
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
      * In the template where the url is to be used, 
        * `href="{{ book.get_absolute_url  }}"`
          * Django will call this and get back the url based on the method in the class (models.py))
    * save()
      * `Model.save(force_insert=False, force_update=False, using=DEFAULT_DB_ALIAS, update_fields=None)`
      * [What happens when you save?](https://docs.djangoproject.com/en/3.2/ref/models/instances/#what-happens-when-you-save)
      * In case the save method is overwritten call `super().save()` after the custom statements
      * `from django.utils.text import slugify`
      * `def save(self, *args, **kwargs):`
        * `self.slug = `
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
        * order_by() : By default, results returned by a QuerySet are ordered by the ordering tuple given by the ordering option in the model’s Meta. You can override this on a per-QuerySet basis by using the order_by method.
          * `Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')`
          * You can also order by query expressions by calling asc() or desc() on the expression:
          * `Entry.objects.order_by(Coalesce('summary', 'headline').desc())`
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
  * db_index : If True, a database index will be created for this field.
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
  * Querying Related Models
    * Main Table that contains a foreign Key
      * books_by_rowling = Book.objects.filter(author__last_name="Rowling")
      * books_by_rowling = Book.objects.filter(author__last_name__contains="ling")
      * author = field in Book Model
      * last_name = field in Author Model
      * contains = modifier
    * Foreign Key Table with data from Main table
      * jkr = Author.objects.get(first_name="J.K.")
      * jkr.book_set.all() # returns all books (Book Table) written by author (author Table) starting with first name J.K.
      * book_set = objects
      * book_set = class name (Book) in lowercase + _set
      * set related_name="books" in the Foreign Key entry in the Book Model to change the reference in the Author model
      * jkr.books.all() = returns all books
  * [get_object_or_404()](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#get-object-or-404)
    * Calls _get()_ on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception.
    * get_object_or_404(Book, pk=id) # from django.shortcuts import get_object_or_404
    * `get_object_or_404(klass, *args, **kwargs)`
    * Required arguments
      * klass : A Model class, a Manager, or a QuerySet instance from which to get the object.
        * passing a Queryset
        * `queryset = Book.objects.filter(title__startswith='M')
get_object_or_404(queryset, pk=1)`
      * **kwargs : Lookup parameters, which should be in the format accepted by get() and filter().
  * [get_list_or_404()](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#get-list-or-404)
    * Returns the result of _filter()_ on a given model manager cast to a list, raising Http404 if the resulting list is empty.
    * Required arguments
      * klass : A Model class, a Manager, or a QuerySet instance from which to get the list.
      * **kwargs : Lookup parameters, which should be in the format accepted by get() and filter().

### SlugField
- In models.py
  - define a field for slug
  - `slug = models.SlugField(default="", null=False)`
  - `from django.utils.text import slugify`
  - Overwrite the default save method in the Model class:
    - `def save(self, 8args, **kwargs):`
      - `self.slug = slugify(self.title)` 
      - `super().save(8args, **kwargs)`

## [Aggregation](https://docs.djangoproject.com/en/3.2/topics/db/aggregation/)
- Django provides two ways to generate aggregates
- aggregate()
  - The first way is to generate summary values over an entire QuerySet
  - sometimes you will need to retrieve values that are derived by summarizing or aggregating a collection of objects
  - `from django.db.models import Avg
  Book.objects.all().aggregate(Avg('price'))`
  - `Book.objects.aggregate(Avg('price'))`
  - aggregate() is a terminal clause for a QuerySet that, when invoked, returns a dictionary of name-value pairs
  - `Book.objects.aggregate(average_price=Avg('price'))`
- annonate()
  - The second way to generate summary values is to generate an independent summary for each object in a QuerySet
  - Annotates each object in the QuerySet with the provided list of query expressions. An expression may be a simple value, a reference to a field on the model (or any related models), or an aggregate expression (averages, sums, etc.) that has been computed over the objects that are related to the objects in the QuerySet.
  - Per-object summaries can be generated using the annotate() clause
  - When an annotate() clause is specified, each object in the QuerySet will be annotated with the specified values.
  - `q = Book.objects.annotate(Count('authors'))`
  - `q[0].authors__count`
  - `q[1].authors__count`
  - Each argument to annotate() is an annotation that will be added to each object in the QuerySet that is returned.
### [Aggregation Methods](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#aggregation-functions)
- Avg : 
- Count
- Max
- Min
- Sum
- StdDev
- Variance
- from django.db.models import Avg, Count, Max, Min ....
- `Book.objects.all().aggregate(Avg('price'))`
- Use order_by() to order the dataset received from the database.


### Overwriting predefined model methods
- It’s important to remember to call the superclass method – that’s that super().save(*args, **kwargs) business – to ensure that the object still gets saved into the database. If you forget to call the superclass method, the default behavior won’t happen and the database won’t get touched.
- It’s also important that you pass through the arguments that can be passed to the model method – that’s what the *args, **kwargs bit does. Django will, from time to time, extend the capabilities of built-in model methods, adding new arguments. If you use *args, **kwargs in your method definitions, you are guaranteed that your code will automatically support those arguments when they are added.
- Overridden model methods are not called on bulk operations.


