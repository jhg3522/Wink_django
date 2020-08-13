from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns= [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signup, name='login'),
    path('logout/', views.signup, name='logout'),
]