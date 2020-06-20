from django.contrib import admin
from django.urls import path
from . import views

app_name='chat'
urlpatterns = [
    path('', views.ChattingLV.as_view(), name = 'index'),
    path('<str:room_name>/<str:room_pass>/', views.room, name='room'),
]
#path('', views.ChattingLV.as_view(), name = 'index'),
