from django.contrib import admin
from bookmark.models import Bookmark
# Register your models here.

@admin.register(Bookmark)
class BookmarkAdim(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
