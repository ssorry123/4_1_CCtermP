from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chatting(models.Model):
	title = models.CharField('TITLE', max_length=100, unique=True, blank=False, null=False)
	password = models.CharField('PASSWORD', max_length=15 ,unique=False, null=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	
	def get_password(self):
		return self.password
	def __str__(self):
		return self.title
