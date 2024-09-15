from django.contrib import admin
from blogs.models import Post
# Register your models here.
class CheckUserPosts(admin.ModelAdmin):
    list_display = ('blog_title','blog_author','blog_content','blog_image','blog_created_at')

admin.site.register(Post,CheckUserPosts)