from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "author", "is_deleted", "created_time", "last_updated_time")
    ordering = ("-id",)

#admin.site.register(Article, ArticleAdmin)
