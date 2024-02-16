from django.contrib import admin

from materials.models import Course, Lessons


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'image',)
    search_fields = ('name',)


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'image', 'link', 'course')
    search_fields = ('name', 'course')
