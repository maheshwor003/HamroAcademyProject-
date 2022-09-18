from tkinter import Widget
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
  course_number=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Course Number"}))
  INTEGER_CHOICES= [tuple([x,x]) for x in range(1,100)]
  max_numb_students= forms.IntegerField(label="Maximum Number Of Students", widget=forms.Select(choices=INTEGER_CHOICES))
  instructors = forms.ModelMultipleChoiceField(
    queryset=Instructor.objects.all(),
    widget=forms.CheckboxSelectMultiple
  )
  short_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"short name"}))


  class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'max_numb_students', 'instructors','short_name']


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'courses']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'department', 'num_class_in_week']
