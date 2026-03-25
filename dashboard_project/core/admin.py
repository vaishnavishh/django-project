from django.contrib import admin
from .models import Course, Enrollment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'credits')  
    search_fields = ('name',)          


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'grade', 'date') 
    search_fields = ('user__username', 'course__name') 
    list_filter = ('grade', 'date')                    
