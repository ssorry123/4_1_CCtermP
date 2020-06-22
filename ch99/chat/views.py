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

class ChattingLV(ListView, LoginRequiredMixin):
	model = Chatting
	template_name = 'chat/index.html'
	
class ChattingCreateView(LoginRequiredMixin, CreateView):
	model = Chatting
	fields = ['title', 'password']
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
	fields = ['title', 'password']
	success_url = reverse_lazy('chat:index')
	
class ChattingDeleteView(OwnerOnlyMixin, DeleteView):
	model = Chatting
	success_url = reverse_lazy('chat:index')


def chatting(request):
    return render(request, 'chat/chatting.html', {})

def room(request,room_name):
	return render(request, 'chat/room.html',{
		'room_name_json':mark_safe(json.dumps(room_name)),
		})

def room1(request, room_name, room_pass):
	# 방 이름과 방 비밀번호를 일치하게 입력하였는지 확인
	u_title=str(room_name)	# 사용자가 입력한 방 이름
	u_password=str(room_pass)	# 사용자가 입력한 방 비밀번호
	print(u_title)	# 확인용 출력
	print(u_password)	# 확인용 출력
	# 실제 방이름에 해당하는 비밀번호
	# 방이름에 해당하는 객체가 존재하지 않으면 에러 발생
	print(Chatting.objects.get(title=u_title))
	password = Chatting.objects.get(title=u_title).get_password()	
	print(password)
	print(password==u_password)
	# 비밀번호가 일치하면 채팅 서버 실행(소켓 연결)
	if password==u_password:
		return render(request, 'chat/room.html', {
			'room_name_json': mark_safe(json.dumps(room_name)),
			'room_pass_json': mark_safe(json.dumps(room_pass)),
			})

	# 방 이름에 해당하는 객체가 존재하지 않으면 에러 발생
	# 방이름에 해당하는 객체가 있어도 비밀번호가 틀리면 에러 발생
	# 가벼운 수준의 완벽한 보안.
	return None




