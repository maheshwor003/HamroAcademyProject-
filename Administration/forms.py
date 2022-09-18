from tkinter.ttk import Style
from django.forms import ModelForm
from. models import *
from django import forms


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'r_number',
            'seating_capacity'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'uid',
            'name'
        ]


class MeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTime
        fields = [
            'pid',
            'time',
            'day'
        ]
        widgets = {
            'pid': forms.TextInput(),
            'time': forms.Select(),
            'day': forms.Select(),
        }


class CourseForm(ModelForm):
  error_css_class='error-field'
  required_css_class='requiredfield'
  course_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Course Name"}))
  instructors = forms.ModelMultipleChoiceField(
        queryset=Instructor.objects.all(),
        widget=forms.CheckboxSelectMultiple)
  
  class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'max_numb_students', 'instructors']


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'courses']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'department', 'num_class_in_week']
