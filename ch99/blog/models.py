from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
	title = models.CharField(verbose_name='TITLE', max_length=50)
	slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
	description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
	content = models.TextField('CONTENT')
	create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
	modify_dt = models.DateTimeField('MODIFY DATE', auto_now = True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
	
	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'
		db_table = 'blog_posts'
		ordering = ('-modify_dt',)
		
	def __str__(self):
		return self.title
	
	# 이 메소드가 정의된 객체를 지칭하는 URL을 반환
	# reverse함수는 URL 패턴을 만들어주는 장고의 내장 함수
	def get_absolute_url(self):
		return reverse('blog:post_detail', args=(self.slug,))
		
	# 장고의 내장 함수 get_previous_by_modify_dt() 호출
	# modify_dt 컬럼 기준으로 최신 포스트를 반환
	def get_previous(self):
		return self.get_previous_by_modify_dt()

	def get_next(self):
		return self.get_next_by_modify_dt()
		
	def save(self, *args, **kwargs):
		self.slug=slugify(self.title, allow_unicode=True)
		super().save(*args, **kwargs)
