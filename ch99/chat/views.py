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

def room(request, room_name, room_pass):
	#아래와 같이 직접접근하지말것 에러남
	#print(request.user.username)
	user=str(request.user.get_username())
	#print(User.get_username(User))
	
	#print(str(User.get_username(self)))

	return render(request, 'chat/room.html', {
		'room_name_json': mark_safe(json.dumps(room_name)),
		'room_pass_json': mark_safe(json.dumps(room_pass)),
		'user':mark_safe(json.dumps(user)),
		})


