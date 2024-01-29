from django.urls import path
from django import urls
from .import views

app_name="questionpaper"

urlpatterns=[
    path('', views.dashboard, name="dashboard"),
    path('paper', views.paper, name="paper"),
    path('addquestion', views.addquestion, name="addquestion"),
    path('approve/<int:id>', views.approve, name="approve"),
    path('approvemcq/<int:id>', views.approvemcq, name="approvemcq"),
    path('addmcq', views.addmcq, name="addmcq"),
    path('addkuestion', views.addkuestion, name="addkuestion"),
    
]