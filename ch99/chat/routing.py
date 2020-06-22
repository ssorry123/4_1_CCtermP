# chat/routing.py
from django.urls import re_path

from . import consumers

# 소비자 라우팅을 처리하기 위한 chat/routing.py 작성
# ( chat routing configuration )
websocket_urlpatterns = [
	# /ws/chat/room_name
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]
