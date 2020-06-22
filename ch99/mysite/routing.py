# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

# chat/routing.py에서 작성한 파일을 Django가 인식할 수 있도록
# mysite/routing.py 작성 ( root routing configuration )

ASGI_APPLICATION = "mysite.routing.application"
'''
 라우터는 그 자체로 유효한 asgi 어플리케이션이고 중첩으로 작성 가능
 channels는 단일 root application(ProtocolTypeRouter)를 정의하여
 이에 대한 경로를 ASGI_APPLICATION 설정으로 제공하기를 기대함.
 settings에 ASGI_APPLICATION 추가
 '''
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    
    # 더 많은 프로토콜 관련 라우팅 중첩
    'websocket': AuthMiddlewareStack(
        URLRouter(
			chat.routing.websocket_urlpatterns
        )
    ),
})
'''
chat/routing.py
websocket_urlpatterns = [
	# /ws/chat/room_name
	re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),]
'''

'''
#간단한 설명
-ProtocolTypeRouter
channels.routing.ProtocolTypeRouter 라우팅 파일은
ASGI 애플리케이션 스택에서 가장 상위에 있는 계층입니다.
이는 현재 scope에 있는 type 값을 기준으로 다른 ASGI 애플리케이션 중 하나로 분기할 수 있습니다.

-URLRouter
channels.routing.URLRouter는 HTTP 또는 WebSocket 타입의 연결을 라우팅합니다.

self.scope['url_route'] : {'args':(), 'kwargs':{'room_name' : 'lobby'}}
['url_route']는 args와 kwargs를 key로 갖는 dictionary입니다.

self.scope['url_route']['kwargs'] : {'room_name' : 'lobby' }
['url_route']['kwargs']는 kwargs는 정규표현식에서 작성된 이름과
	그 값을 key와 value로 갖는 dictionary입니다.

self.scope['url_route']['kwargs']['room_name'] : lobby
['url_route']['kwargs']['room_name']는 kwargs의 
	여러 key중에서 room_name의 value를 얻는 코드입니다.
'''

'''
 클라이언트와 Channels 개발 서버와 연결이 맺어질 때,
 ProtocolTypeRouter를 가장 먼저 조사하여 어떤 타입의 연결인지 구분
 만약 웹소켓 연결이라면 AuthMiddlewareStack으로 이어진다.
 
 AuthMiddlewareStack은 현재 인증된 사용자에 대한 참조로 scope를 결정한다.
 이는 Django에서 view함수에서 request 요청을 결정하는
 AuthenticationMiddleware와 유사한 방식이다.
 그결과 URLRouter로 연결된다
 
 URLRouter는 작성한 url패턴을 기반으로,
 특정 소비자의 라우트 연결 HTTP path를 조사한다
'''

