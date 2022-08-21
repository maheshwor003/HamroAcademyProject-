from django.contrib import admin
from .models import Course, Instructor


# class CourseContent(admin.ModelAdmin):
#      list_display= ('course_number','course_name','max_numb_students','instructors')

# class InstructorDetails(admin.ModelAdmin):
#      list_sdisplay= ('course_id','instructor_id')

admin.site.register(Course)
admin.site.register(Instructor)
# Register your models here.
