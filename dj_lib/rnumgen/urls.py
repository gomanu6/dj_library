from django.urls import path

from . import views


urlpatterns = [
    path('', views.rnum_index, name='rnum_index')
]