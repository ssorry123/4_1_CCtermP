from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.

# ListView
# ListView 제네릭뷰를 상속받아 PostLV 클래스형 뷰를 정의
class PostLV(ListView) :
	model = Post
	# 지정하지 않으면 디폴트 템플릿  'blog/post_list.html'
	template_name = 'blog/post_all.html'
	# 넘겨주는 객체 리스트 변수명 posts로 지정
	# 디폴트 변수명 'object_list' 역시 사용 가능
	context_object_name = 'posts'
	# 한 페이지에 보여주는 객체 리스트 2, 속성을 정의하면
	# 장고 제공 페이징 기능 사용 가능
	paginate_by = 2

# DetailView
class PostDV(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

# ArchiveView
class PostAV(ArchiveIndexView):
	model = Post
	date_field = 'modify_dt'
	template_name = 'blog/post_archive.html'
	
class PostYAV(YearArchiveView):
	model = Post
	date_field = 'modify_dt'
	make_object_list = True
	template_name = 'blog/post_archive_year.html'

class PostMAV(MonthArchiveView):
	model = Post
	date_field = 'modify_dt'
	template_name = 'blog/post_archive_month.html'

class PostDAV(DayArchiveView):
	model = Post
	date_field = 'modify_dt'
	template_name = 'blog/post_archive_day.html'
	
class PostTAV(TodayArchiveView):
	model = Post
	date_field = 'modify_dt'
	template_name = 'blog/post_archive_year.html'
