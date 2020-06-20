from django.urls import path
# URLconf에서 뷰를 호출하므로, 뷰 모듈의 관련 클래스를 임포트
#from bookmark.views import BookmarkLV, BookmarkDV
from bookmark import views

app_name = 'bookmark'
urlpatterns = [
	path('', views.BookmarkLV.as_view(), name = 'index'),
	path('<int:pk>/', views.BookmarkDV.as_view(), name = 'detail'),
	

	# /bookmark/add/
	path('add/', views.BookmarkCreateView.as_view(), name="add",),

	# /bookmark/change/
	path('change/', views.BookmarkChangeLV.as_view(), name="change",),

	# /bookmark/99/update/
	path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update",),

	# /bookmark/99/delete/
	path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete",),
]
'''
# /bookmark/add/
path('add/', views.BookmarkCreateView.as_view(), name="add",)

# /bookmark/change/
path('change/', views.BookmarkChangeLV.as_view(), name="change",),

# /bookmark/99/update/
path('<int:pk>/update/', views.BookmarkDeleteView.as_view(), name="update",),

# /bookmark/99/delete/
path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete",),
'''
