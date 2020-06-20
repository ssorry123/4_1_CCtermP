from django.contrib import admin
from chat.models import Chatting
# Register your models here.

@admin.register(Chatting)
class BookmarkAdim(admin.ModelAdmin):
    list_display = ('id', 'title', 'password')
