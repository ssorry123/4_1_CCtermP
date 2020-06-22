from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chatting(models.Model):
	title = models.CharField('TITLE', max_length=100, unique=True, blank=False, null=False)
	password = models.CharField('PASSWORD', max_length=15 ,unique=False, null=False, blank=False)
	member = models.CharField('MEMBER', max_length=1000, unique=False, null = True, blank = True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	
	def get_member(self, member_name):
		members=self.member
		# members가 None이면 모두에게 허용한다.
		if members==None:
			return True
		# members에 허용한 사용자가 있는지 확인한다.
		# 허용하지 않은 사용자이면 -1를 반환한다(str에 member_name이 존재하는지 파이썬 문자열 함수)
		# 존재하면 offset 반환, 존재하지 않으면 -1 반환
		print(1);print(member_name);print(members);print(2)
		ret = members.find(member_name)
		# 허용된 사용자일 경우 True 반환
		if ret!=-1:
			return True
		else:
			return False
			
	# 모델의 주인을 반환
	def get_owner(self):
		return str(self.owner)
	# 모델의 비밀번호를 반환
	def get_password(self):
		return str(self.password)
	# 모델의 객체만 변수로 사용될 경우 모델(채팅방)의 title만 반환
	def __str__(self):
		return str(self.title)
