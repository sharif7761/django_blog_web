
from django.urls import path
from .import views

urlpatterns = [
    path('', views.authlogin,name="login"),
    path('registration', views.authregistration,name="registration"),
    path('forgotPassword', views.forgotPassword,name="forgotPassword"),
    path('logout', views.userlogout,name="logout"),
        
]
