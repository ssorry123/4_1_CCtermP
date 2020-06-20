from django.contrib import admin
from chat.models import Chatinfo
# Register your models here.

@admin.register(Chatinfo)
class BookmarkAdim(admin.ModelAdmin):
    list_display = ('id', 'title', 'password')
