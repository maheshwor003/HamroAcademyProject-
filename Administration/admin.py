from django.contrib import admin
from .models import Course, Instructor,Room,Section,Department,Meetingtime



# class InstructorDetails(admin.ModelAdmin):
#      list_sdisplay= ('course_id','instructor_id')

@admin.register(Course)
class CourseContent(admin.ModelAdmin):
      list_display= ('course_code','course_name','max_numb_students','instructors')

admin.site.register(Instructor)
admin.site.register(Room)
admin.site.register(Meetingtime)
admin.site.register(Department)
admin.site.register(Section)


# Register your models here.
