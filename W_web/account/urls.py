from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns= [
    path('signup/', views.sign, name='sign'),
    path('login/', views.signup, name='login'),
    path('logout/', views.signup, name='logout'),
    path('signup/',views.UserCreateView.as_view(),name='join'),
    path('join/',views.signup , name='sign'),
]