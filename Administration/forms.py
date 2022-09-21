# from django import forms
# from .models import Course

# class CourseForm(forms.ModelForm):
#   #seller = forms.ModelChoiceField(queryset=Seller.objects.all(), initial=3, widget=AutoCompleteWidget(url='/custom-json-jquery', initial_display='amazon'))
#   #seller = forms.ModelChoiceField(label='Seller', queryset=Seller.objects.all(),widget=AutoCompleteWidget)
#   #weight = forms.CharField(max_length=254,label='Largeur',widget=forms.TextInput({'class': 'form-control','placeholder': ''}))
#   #length = forms.CharField(max_length=254,label='Longueur',widget=forms.TextInput({'class': 'form-control','placeholder': ''}))
#   #height = forms.CharField(max_length=254,label='Hauteur',widget=forms.TextInput({'class': 'form-control','placeholder': ''}))
#   #width = forms.CharField(max_length=254,label='Poids',widget=forms.TextInput({'class': 'form-control','placeholder': ''}))
#   class Meta:
#     model = Course
#     fields = '__all__'
#     # [
#     # 'course_code','course_name','max_numb_students','instructors'
#     # ]

from django import forms
from django.forms import ModelForm
from. models import *


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = [
            'r_number',
            'seating_capacity'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructors
        fields = [
            'uid',
            'name'
        ]


class MeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTimes
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
    class Meta:
        model = Courses
        fields = ['course_number', 'course_name',
                  'max_numb_students', 'instructors']


class DepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = ['dept_name', 'courses']


class SectionForm(ModelForm):
    class Meta:
        model = Sections
        fields = ['section_id', 'department', 'num_class_in_week']
