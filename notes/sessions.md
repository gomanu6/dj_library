
### Sessions
- stores data on the server side and abstracts the sending and receiving of cookies
- Django stores sessions in your database (using the model django.contrib.sessions.models.Session).
- Session data is stored in a database table named django_session .
- Session data can also be stored in the Django cache. [Django Cache Framework](https://docs.djangoproject.com/en/3.2/topics/cache/)
- By default, Django serializes session data using JSON. You can use the SESSION_SERIALIZER setting to customize the session serialization format.
- Session Object Guidelines
  - Use normal Python strings as dictionary keys on request.session. This is more of a convention than a hard-and-fast rule.
  - Session dictionary keys that begin with an underscore are reserved for internal use by Django.
  - Don’t override request.session with a new object, and don’t access or set its attributes. Use it like a Python dictionary.
- As users create new sessions on your website, session data can accumulate in your session store. If you’re using the database backend, the django_session database table will grow. If you’re using the file backend, your temporary directory will contain an increasing number of files.
- Django does not provide automatic purging of expired sessions. Therefore, it’s your job to purge expired sessions on a regular basis. Django provides a clean-up management command for this purpose: [clearsessions](https://docs.djangoproject.com/en/3.2/ref/django-admin/#django-admin-clearsessions). It’s recommended to call this command on a regular basis, for example as a daily cron job.
- `django-admin clearsessions` : Can be run as a cron job or directly to clean out expired sessions.
- We cannot store objects in sessions as the objects may contain methods and these methos cannot be serialised in JSON. We should store primitive values or dictionaries in session
- 

### Session Types
- Database backed sessions
  - If you want to use a database-backed session, you need to add 'django.contrib.sessions' to your INSTALLED_APPS setting.
  - Once you have configured your installation, run manage.py migrate to install the single database table that stores session data.
- Cached Sessions
  - Set SESSION_ENGINE to "django.contrib.sessions.backends.cache" for a simple caching session store.
  - OR
  - For persistent, cached data, set SESSION_ENGINE to "django.contrib.sessions.backends.cached_db".
  - Both session stores are quite fast, but the simple cache is faster because it disregards persistence.
- File-based sessions
  - To use file-based sessions, set the SESSION_ENGINE setting to "django.contrib.sessions.backends.file".
  - You might also want to set the SESSION_FILE_PATH setting (which defaults to output from tempfile.gettempdir(), most likely /tmp) to control where Django stores session files. Be sure to check that your Web server has permissions to read and write to this location.
- cookie based sessions
  - To use cookies-based sessions, set the SESSION_ENGINE setting to "django.contrib.sessions.backends.signed_cookies". The session data will be stored using Django’s tools for cryptographic signing and the SECRET_KEY setting.
  - It’s recommended to leave the SESSION_COOKIE_HTTPONLY setting on True to prevent access to the stored data from JavaScript.
  - If the SECRET_KEY is not kept secret and you are using the PickleSerializer, this can lead to arbitrary remote code execution.

### [How to use Sessions](https://docs.djangoproject.com/en/3.2/topics/http/sessions/)
- settings.py
  - 'django.contrib.sessions.middleware.SessionMiddleware' -> should be present in MIDDLEWARE
  - `MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',`
  - INSTALLED_APPS = [..., django.contrib.sessions, ...]
  



### Sessions in Views
- When SessionMiddleware is activated, each HttpRequest object – the first argument to any Django view function – will have a session attribute, which is a dictionary-like object.
- You can read it and write to request.session at any point in your view. You can edit it multiple times.
- Base Class for al Session Objects : backends.base.SessionBase
- Methods
  - __getitem__(key) : Example: fav_color = request.session['fav_color']
  - __setitem__(key, value) : Example: request.session['fav_color'] = 'blue'
  - __delitem__(key) : Example: del request.session['fav_color']. This raises KeyError if the given key isn’t already in the session.
  - __contains__(key) : Example: 'fav_color' in request.session
  - get(key, default=None) : Example: fav_color = request.session.get('fav_color', 'red')
  - pop(key, default=__not_given) : Example: fav_color = request.session.pop('fav_color', 'blue')
  - keys()
  - items()
  - setdefault()
  - clear()
  - It also has these methods:
  - flush() : Deletes the current session data from the session and deletes the session cookie. This is used if you want to ensure that the previous session data can’t be accessed again from the user’s browser (for example, the django.contrib.auth.logout() function calls it).
  - set_test_cookie() : Sets a test cookie to determine whether the user’s browser supports cookies. Due to the way cookies work, you won’t be able to test this until the user’s next page request. See Setting test cookies below for more information.
  - test_cookie_worked() : Returns either True or False, depending on whether the user’s browser accepted the test cookie. Due to the way cookies work, you’ll have to call set_test_cookie() on a previous, separate page request. See Setting test cookies below for more information.
  - delete_test_cookie() : Deletes the test cookie. Use this to clean up after yourself.
  - get_session_cookie_age() : Returns the age of session cookies, in seconds. Defaults to SESSION_COOKIE_AGE.
  - set_expiry(value) : Sets the expiration time for the session. You can pass a number of different values:
    - If value is an integer, the session will expire after that many seconds of inactivity. For example, calling request.session.set_expiry(300) would make the session expire in 5 minutes.
    - If value is a datetime or timedelta object, the session will expire at that specific date/time. Note that datetime and timedelta values are only serializable if you are using the PickleSerializer.
    - If value is 0, the user’s session cookie will expire when the user’s Web browser is closed.
    - If value is None, the session reverts to using the global session expiry policy.
    - Reading a session is not considered activity for expiration purposes. Session expiration is computed from the last time the session was modified.
  - get_expiry_age() : Returns the number of seconds until this session expires. For sessions with no custom expiration (or those set to expire at browser close), this will equal SESSION_COOKIE_AGE.
    - This function accepts two optional keyword arguments:
      - modification: last modification of the session, as a datetime object. Defaults to the current time.
      - expiry: expiry information for the session, as a datetime object, an int (in seconds), or None. Defaults to the value stored in the session by set_expiry(), if there is one, or None.
  - get_expiry_date() : Returns the date this session will expire. For sessions with no custom expiration (or those set to expire at browser close), this will equal the date SESSION_COOKIE_AGE seconds from now.
    - This function accepts the same keyword arguments as get_expiry_age().
  - get_expire_at_browser_close() : Returns either True or False, depending on whether the user’s session cookie will expire when the user’s Web browser is closed.
  - clear_expired() : Removes expired sessions from the session store. This class method is called by clearsessions.
  - cycle_key() : Creates a new session key while retaining the current session data. django.contrib.auth.login() calls this method to mitigate against session fixation.

### Some Options
- SESSION_COOKIE_AGE = => in seconds, Default: 1209600 (2 weeks, in seconds)
- SESSION_COOKIE_DOMAIN : The domain to use for session cookies. Set this to a string such as "example.com" for cross-domain cookies, or use None for a standard domain cookie. Default: None
- SESSION_COOKIE_NAME : Default: 'sessionid'. This can be whatever you want (as long as it’s different from the other cookie names in your application).
- SESSION_COOKIE_PATH : Default: '/'. This should either match the URL path of your Django installation or be parent of that path.This is useful if you have multiple Django instances running under the same hostname. They can use different cookie paths, and each instance will only see its own session cookie.
- SESSION_ENGINE : Default: 'django.contrib.sessions.backends.db'
- SESSION_EXPIRE_AT_BROWSER_CLOSE : Default: False. [Browser-length sessions vs. persistent sessions.](https://docs.djangoproject.com/en/3.2/topics/http/sessions/#browser-length-vs-persistent-sessions)
- SESSION_SERIALIZER : Default: 'django.contrib.sessions.serializers.JSONSerializer'. [See Session serialization for details](https://docs.djangoproject.com/en/3.2/topics/http/sessions/#session-serialization)
- SESSION_SAVE_EVERY_REQUEST : Default: False. If this is False (default), then the session data will only be saved if it has been modified – that is, if any of its dictionary values have been assigned or deleted. Empty sessions won’t be created, even if this setting is active.
- SESSION_FILE_PATH : Default: None. If you’re using file-based session storage, this sets the directory in which Django will store session data. When the default value (None) is used, Django will use the standard temporary directory for the system.
