from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns= [
    path('',views.main_index,name='main_index'),
    path('generic/',views.generic, name='generic'),
    path('post_list/',views.post_list,name='post_list'),
    path('board/',views.board,name='board'),
    path('board/<int:documnet.id>',views.detail,name='detail'),
]