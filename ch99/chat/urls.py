from django.contrib import admin
from django.urls import path
from . import views

app_name='chat'
urlpatterns = [

	### 채팅방 메인 화면 ###
	# /chat/
    path('', views.ChattingLV.as_view(), name = 'index'),
    
    ### 채팅방 관리 url ###
    
    # /chat/add/
    path('add/', views.ChattingCreateView.as_view(), name="add"),
    
    # /chat/change/
    path('change/', views.ChattingChangeLV.as_view(), name="change"),
    
    # /chat/00/update
    path('<int:pk>/update/', views.ChattingUpdateView.as_view(), name="update"),
    
    # /chat/00/delete
    path('<int:pk>/delete/', views.ChattingDeleteView.as_view(), name="delete"),
    
    
    ### 채팅방 접속 url ###
    
    # /chat/room_name/ 보안 문제로 해제, 비밀번호 없이 접속 가능
    #path('<str:room_name>/', views.room, name='room'),
    
	# /chat/room_name/room_pass/ 보안 문제로 해제, 방 주인이 blacklist를 설정해도 접속 가능
    #path('<str:room_name>/<str:room_pass>/', views.room, name='room'),
    
	# /chat/room_name/room_pass/room_nick/ 비밀번호 및 방 주인의 blacklist 기능 사용 가능
    path('<str:room_name>/<str:room_pass>/<str:room_nick>/', views.room, name='room'),
]

