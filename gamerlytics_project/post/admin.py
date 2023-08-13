from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    search_fields = ('title', 'content')
    list_filter = ('pub_date', 'author')
