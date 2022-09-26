from tkinter import Widget
from tkinter.ttk import Style
from django.forms import ModelForm

from SystemLogin.models import User
from TeacherAndStudent.models import Student
from. models import *
from django import forms




class RoomForm(ModelForm):
 error_css_class='error-field'
 required_css_class='requiredfield'
 r_number=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Room number"}))
 INTEGER_CHOICES= [tuple([x,x]) for x in range(1,100)]
 seating_capacity= forms.IntegerField(label="Total number of seats", widget=forms.Select(choices=INTEGER_CHOICES))
 class Meta:
        model = Room
        fields = [
            'r_number',
            'seating_capacity'
        ]


class InstructorForm(ModelForm):
 error_css_class='error-field'
 required_css_class='requiredfield'
 uid=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":" id"}))
 name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Teachers Name"}))
 class Meta:
        model = Instructor
        fields = ['uid','name']

class StudentForm(ModelForm):
 error_css_class='error-field'
 required_css_class='requiredfield'
 USN=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":" USN"}))
 name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":" Student Name"}))
 YEARS= [x for x in range(0,20)]
 DOB= forms.DateField(label='Birthdate', widget=forms.SelectDateWidget)
 class Meta:
        model = Student
        fields = [
            'user',
            'class_id',
            'USN',
            'name',
            'sex',
            'DOB',
        ]

class MeetingTimeForm(ModelForm):
 error_css_class='error-field'
 required_css_class='requiredfield'
 pid=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Meeting id"}))
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

class DocumentForm(ModelForm):
   class Meta:
        model = Document
        fields = ('description','document',)
        


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
 

  class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'max_numb_students', 'instructors']


class DepartmentForm(ModelForm):
  error_css_class='error-field'
  required_css_class='requiredfield'
  dept_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Department Name"}))
  courses = forms.ModelMultipleChoiceField(
    queryset=Course.objects.all(),
    widget=forms.CheckboxSelectMultiple
  )

  class Meta:
    model = Department
    fields = ['dept_name', 'courses']


class SectionForm(ModelForm):
  error_css_class='error-field'
  required_css_class='requiredfield'
  section_id=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Section ID"}))
  INTEGER_CHOICES= [tuple([x,x]) for x in range(1,100)]
  num_class_in_week= forms.IntegerField(label="Total number of class in a week", widget=forms.Select(choices=INTEGER_CHOICES))
  class Meta:
        model = Section
        fields = ['section_id', 'department', 'num_class_in_week','instructor','course','meeting_time','room']