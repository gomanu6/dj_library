from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_reports, name='all_reports'),
    path('<int:report_no>/', views.report, name='single_report')

]