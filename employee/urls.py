
from django.urls import path
from .import views

urlpatterns = [
    path('', views.employee,name="employee_home"),
    path('profile', views.profile,name="employee_profile"),
   
]
