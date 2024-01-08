from django.contrib import admin
from .models import Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "date_updated"]
    list_editable = ["description", ]
    search_fields = ['title']
    list_per_page = 10