from django.contrib import admin
from django.urls import path
from . import views

app_name='chat'
urlpatterns = [
    path('', views.ChattingLV.as_view(), name = 'index'),
    
    # /chat/add/
    path('add/', views.ChattingCreateView.as_view(), name="add"),
    
    # /chat/change/
    path('change/', views.ChattingChangeLV.as_view(), name="change"),
    
    # /chat/00/update
    path('<int:pk>/update/', views.ChattingUpdateView.as_view(), name="update"),
    
    # /chat/00/delete
    path('<int:pk>/delete/', views.ChattingDeleteView.as_view(), name="delete"),
    
    path('<str:room_name>/', views.room, name='room'),
    
    # 채팅방 접속, /chat/chatroomname/passwordqwer/
    path('<str:room_name>/<str:room_pass>/', views.room1, name='room1'),
]
#path('', views.ChattingLV.as_view(), name = 'index'),
