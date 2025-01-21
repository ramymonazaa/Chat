from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.show_rooms, name='rooms'),
    path('<slug:slug>/', views.show_room, name='room'),
    path('contact/<str:username>/', views.contact, name='contact'),
    path('create room/', views.create_room, name='create_room'),
]
