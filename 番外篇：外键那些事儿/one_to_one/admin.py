from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class Profile(admin.ModelAdmin):
    def username(self, obj):
        return obj.user.username
    username.short_description = 'username'

    list_display = ['id', 'nickname', 'username']
