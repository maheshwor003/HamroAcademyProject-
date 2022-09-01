from django.contrib import admin
from .models import Course, Instructor


# class InstructorDetails(admin.ModelAdmin):
#      list_sdisplay= ('course_id','instructor_id')

@admin.register(Course)
class CourseContent(admin.ModelAdmin):
    list_display = ('course_code', 'course_name',
                    'max_numb_students', 'instructors')


admin.site.register(Instructor)
# Register your models here.
