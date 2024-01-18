
from django.urls import path
from django import urls
from .import views

app_name="accounts"

urlpatterns=[
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('', views.logout, name="logout"),
    path('userprofile', views.userprofile, name="userprofile"),
    path('passwordchange', views.passwordchange, name="passwordchange"),
    
]