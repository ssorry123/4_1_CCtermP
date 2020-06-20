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
	

def chatting(request):
    return render(request, 'chat/chatting.html', {})



def room(request, room_name, room_pass):
	print(request.user.username)
	user=str(request.user.username)
	#print(User.get_username(User))
	
	#print(str(User.get_username(self)))

	return render(request, 'chat/room.html', {
		'room_name_json': mark_safe(json.dumps(room_name)),
		'room_pass_json': mark_safe(json.dumps(room_pass)),
		'user':mark_safe(json.dumps(user)),
		})


