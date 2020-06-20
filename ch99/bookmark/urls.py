from django.urls import path
# URLconf에서 뷰를 호출하므로, 뷰 모듈의 관련 클래스를 임포트
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark'
urlpatterns = [
	path('', BookmarkLV.as_view(), name = 'index'),
	path('<int:pk>/', BookmarkDV.as_view(), name = 'detail'),
]
