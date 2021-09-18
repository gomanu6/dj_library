from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:subject>/', views.subject_no, name='subject_no'),
    path('<str:subject>/', views.subject, name='subject'),

]
