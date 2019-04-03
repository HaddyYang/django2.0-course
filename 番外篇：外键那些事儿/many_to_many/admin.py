from django.contrib import admin
from .models import Author, Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name']
    filter_horizontal = ('authors',)
