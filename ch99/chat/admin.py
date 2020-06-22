from django.contrib import admin
from chat.models import Chatting
# Register your models here.

# admin에 등록 및
# admin에서 어떻게 보일지 등록
@admin.register(Chatting)
class BookmarkAdim(admin.ModelAdmin):
    list_display = ('id', 'title', 'password','member')
