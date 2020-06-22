# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

'''
class ChatConsumer 구현

Channel layer, channel_redis
Channel layer는 의사소통 시스템이다.
이는 많은 소비자들 또는 Django의 다른 부분들과 의사소통을 할 수 있게 해준다.
Channel layer에는 다음과 같은 추상화를 제공한다

1) channel
channel은 메시지를 보낼 수 있는 우편함 개념이다
각 채널은 이름을 갖고 있으며, 누구든지 채널에 메시지를 보낼 수 있다.

2) group
그룹은 이름을 가지며, 그룹 이름을 가진 사용자는 누구나 그룹에 채널을 추가/삭제가 가능하고,
그룹의 모든 채널에게 메시지를 보낼 수 있다.
그러나 그룹에 속한 채널을 나열할 수는 없다.

모든 소비자들은 유일한 채널이름을 자동으로 생성받으며, channel layer를 통해 의사소통 가능
다른 사람들과 소통하기 위하여 room이름을 기반으로한 group에 채널을 추가해야함
그래야 채팅 소비자들은 같은 방안에 있는 다른 소비자들에게 메세지를 보낼 수 있다
웹소켓은 html의 JS코드가 활성화시킨다
'''
# 모든 요청을 받아들이는 동기적인 WebSocket 소비자 역할
class ChatConsumer(WebsocketConsumer):
    def connect(self):
			
		# chat/routing.py에 정의된 URL 파라미터에서 room_name을 얻는다
        # 즉 소비자에게 WebSocket을 열어준다.
        # mysite/setting.py URLRouter
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # 사용자가 작성한 room 이름으로부터 채널의 그룹 이름을 얻는다
        self.room_group_name = 'chat_%s' % self.room_name


		# Join room group
		# 소비자들은 비동기 channel layer 메서드를 호출할 때 동기적으로
		# 받아야 하기 때문에 as_to_sy 같은 wrapper가 필요
		# 모든 channel layer 메소드는 비동기
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        
        # websocket 연결을 받아들임
        self.accept()

    def disconnect(self, close_code):

		# Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    
    
    '''
    아래 두 함수
    클라이언트가 메세지를 등록하면 JS함수가 WebSocket을 통해 소비자에게 메시지 전송
    소비자는 메시지를 받고, room 이름에 대응되는 Group으로 포워드 한다
    따라서 같은 그룹에 있는 모든 소비자는 메시지를 받을 수 있게 된다.
    WebSocket은 check.html, room.html의 JS코드가 활성화 시킵니다
    '''
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']


		# Send message to room group
		# 그룹에게 이벤트를 보낸다
		# 이벤트에는 이벤트를 수신하는 소비자가 호출해야하는
		# 메소드 이름에 대응하는 특별한 type키가 있다
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

		

	# Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))


