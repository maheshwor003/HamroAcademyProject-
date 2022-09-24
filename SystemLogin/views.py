import imp
from django.shortcuts import render, redirect

from Administration.models import Course, Department
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from  TeacherAndStudent.models import *
from  SystemLogin.models import *


def homepage(request):
    mjm = Department.objects.all()
    mj = Homedetails.objects.all()
    mmj = Course.objects.all()
    mmjs = Teacher.objects.all()
    context = {'homepage_view': mj, 'home_depview' :mjm,'courses':mmj,'wws':mmjs}
    return render(request, 'homepage.html', context)

def navbar(request):
    mjm = Department.objects.all()
    mj = Homedetails.objects.all()
    context = {'homepage_view': mj, 'home_depview' :mjm,}
    return render(request, 'navbar.html', context)

def about(request):
    mjm = Department.objects.all()
    mj = Homedetails.objects.all()
    context = {'homepage_view': mj, 'home_depview' :mjm,}
    return render(request, 'about.html', context)

def course(request):
    mj = Homedetails.objects.all()
    mjm = Department.objects.all()
    mmj = Course.objects.all()
    context = {'homepage_view': mj,'home_depview' :mjm,'courses':mmj}
    return render(request, 'course.html', context)

def teacher(request):
    mj = Homedetails.objects.all()
    mjm = Department.objects.all()
    mjms = Teacher.objects.all()
    mmj = Course.objects.all()
    context = {'homepage_view': mj,'home_depview':mjm,'wws' :mjms,'courses':mmj}
    return render(request, 'teacher.html', context)
    

def single(request):
    mj = Homedetails.objects.all()
    mjm = Department.objects.all()
    mjms = Teacher.objects.all()
    mmj = Course.objects.all()
    context = {'homepage_view': mj,'home_depview':mjm,'wws' :mjms,'courses':mmj}
    return render(request, 'single.html', context)
    


def contact(request):
    mj = Homedetails.objects.all()
    mjm = Department.objects.all()
    mjms = Teacher.objects.all()
    mmj = Course.objects.all()
    context = {'homepage_view': mj,'home_depview':mjm,'wws' :mjms,'courses':mmj}
    return render(request, 'contact.html', context)
    


def register(request):
    mj = Homedetails.objects.all()
    mjm = Department.objects.all()
    mjms = Teacher.objects.all()
    mmj = Course.objects.all()
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('homepage')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    context={'homepage_view': mj,'home_depview':mjm,'wws' :mjms,'courses':mmj,'form': form, 'msg': msg}
    return render(request, 'register.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('dashboard')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('studentpage')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacherdashboard')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})
