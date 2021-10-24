from django.contrib import admin

from .models import Report, Employee

# Register your models here.

admin.site.register(Employee)
admin.site.register(Report)

