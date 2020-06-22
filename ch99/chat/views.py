from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from django.views.generic import ListView, DetailView
from .models import Chatting

from django.views.generic import DeleteView, CreateView, UpdateView
from mysite.views import OwnerOnlyMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User


### 채팅방 메인 화면 ###
class ChattingLV(ListView, LoginRequiredMixin):
	model = Chatting
	template_name = 'chat/index.html'


### 채팅방 모델 관리 부분 ###
class ChattingCreateView(LoginRequiredMixin, CreateView):
	model = Chatting
	fields = ['title', 'password','member']
	success_url = reverse_lazy('chat:index')
	
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)
		
class ChattingChangeLV(LoginRequiredMixin, ListView):
	template_name = 'chat/chatting_change_list.html'
	
	def get_queryset(self):
		return Chatting.objects.filter(owner=self.request.user)

class ChattingUpdateView(OwnerOnlyMixin, UpdateView):
	model = Chatting
	fields = ['title', 'password','member']
	success_url = reverse_lazy('chat:index')
	
class ChattingDeleteView(OwnerOnlyMixin, DeleteView):
	model = Chatting
	success_url = reverse_lazy('chat:index')


### 채팅방 접속 부분 ###
def room(request, room_name, room_pass, room_nick):
	cond1=False	#방이름과 비밀번호 확인
	cond2=False	#허용된 멤버 확인
	# 1. 채팅방 객체, 가져오는 과정에서 사용자가 존재하지 않는 방이름을 입력하면 에러 발생
	chat_room=Chatting.objects.get(title=room_name)
	
	
	### 자신이 채팅방의 owner인 경우 당연히 접속 허용
	owner=str(chat_room.get_owner())		# 채팅방 주인 id
	guest=str(request.user.username)	# 채팅방 접속하는 사람 id
	print(owner);print(guest);		# 확인용 출력
	if guest==owner:
		return render(request, 'chat/check.html', {
			'room_name_json': mark_safe(json.dumps(room_name)),
			'room_pass_json': mark_safe(json.dumps(room_pass)),
			'room_nick_json': mark_safe(json.dumps(room_nick)),
			})

	
	### 2. 방 이름과 방 비밀번호를 일치하게 입력하였는지 확인
	u_password = str(room_pass)					# 사용자가 입력한 방 비밀번호
	r_password = str(chat_room.get_password())	# 사용자가 입력한 방의 실제 비밀번호
	print(u_password);print(r_password);print(u_password==r_password)	# 확인용 출력
	if u_password == r_password:
		cond1=True
	
	### 3. 허용된 멤버인지 확인, 사용자의 진짜 id가 아닌, 사용자(guest)가 설정한 nick으로 확인
	# 현재 사용자 id와 현재 사용자의 nick은 다를 수 있다
	# get_member는 bool 반환, user가 채팅 모델의 member에 속하는지 확인
	cond2=chat_room.get_member(room_nick)
	print(cond2)	# 확인용 출력
	
	
	# 조건을 만족할 경우 채팅방 소켓 연결
	if cond1==True and cond2==True:
	#if True:
	# html에서 사용하기 위해 json으로 변환한 후 전달
		return render(request, 'chat/room.html', {
			'room_name_json': mark_safe(json.dumps(room_name)),
			'room_pass_json': mark_safe(json.dumps(room_pass)),
			'room_nick_json': mark_safe(json.dumps(room_nick)),
			})
	
	### 위에 해당하는 것이 없을 경우 None 리턴, 채팅방 접속 불가
	# 3단계 보안
	# 방 이름에 해당하는 객체가 존재하지 않으면 에러 발생
	# 방이름에 해당하는 객체가 있어도 비밀번호가 틀리면 에러 발생
	# 방이름과 비밀번호가 맞아도 자신이 방장에 의해 허용되지 않았으면 에러 발생
	
	# guest가 임의로 url을 /chat/room_name/xxxx/xxxxx/로 접속해서
	# ws/chat/room_name 소켓에 접근하려해도 소켓에 접근하는 방법은
	# /chat/room_name/xxxx/xxxxx 경로뿐이므로 불가능.
	return None

