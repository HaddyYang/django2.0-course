from django.contrib import admin
from .models import SchoolClass, Student

# Register your models here.
@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'class_name', 'class_master']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_class', 'student_name', 'sex']
