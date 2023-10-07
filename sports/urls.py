from django.contrib import admin
from django.urls import path, include
from esports import urls
from sports import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('registration',views.registration,name='registration'),
    path('user_data',views.user_data,name='user_data'),
]

