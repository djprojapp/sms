from django.urls import path
from django import urls
from .import views

app_name="questionpaper"

urlpatterns=[
    path('', views.home, name="home"),
    path('addquestion', views.addquestion, name="addquestion"),
    path('approve/<int:id>', views.approve, name="approve"),
    path('addmcq', views.addmcq, name="addmcq"),
    
]