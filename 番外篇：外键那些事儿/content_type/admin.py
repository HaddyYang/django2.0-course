from django.contrib import admin
from .models import Article, Video, Comment

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'video_name', 'url']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_type', 'object_id', 'content_object', 'text']
