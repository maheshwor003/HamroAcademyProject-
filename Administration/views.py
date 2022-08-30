from django.shortcuts import render
from .models import Course, Instructor
from django.http import JsonResponse
from django.core import serializers
# Create your views here.




def adminpage(request):
    return render (request,'adminpage.html')





def teacher(request):
    return render(request,'teacherpage.html')


def student(request):
    return render(request,'studentpage.html')

def base(request):
    return render (request,'dashboard.html')
def add_teacher(request):
    return render (request,'add-teacher.html')
def all_teacher(request):
    return render (request,'all-teacher.html')
    
# def all_course(request):
#     return render (request,'allcourse.html')
    
def all_course(request):
    subjects=Instructor.objects.all()
    dataread=Course.objects.all()
    context = {'subjects':subjects,'data_read':dataread}
    return render (request,'allcourse.html',context)


def savecourse_data(request):
     if request.method == "POST":
           
           course_code= request.POST.get('course_code')
           course_name= request.POST['course_name']
           max_numb_students=request.POST['max_numb_students']
           instructors= request.POST['instructors']
           ins=Instructor.objects.get(id=instructors)
         
           usr= Course(course_code=course_code,course_name=course_name,max_numb_students=max_numb_students,instructors=ins)
         
           usr.save()
           stud =Course.objects.values()
           student_data =list(stud)
           return JsonResponse({'status':'Save',
           'course_data':student_data})
     else:
           return JsonResponse({'status':0})


def updatecourse_data(request,id):
     if request.method == "POST":
           course_code= request.POST.get('course_code')
           course_name= request.POST['course_name']
           max_numb_students=request.POST['max_numb_students']
           instructors= request.POST['instructors']
           ins=Instructor.objects.get(id=instructors)
           usr= Course.objects.get(id=id)
           usr.course_code=course_code
           usr.course_name=course_name
           usr.max_numb_students=max_numb_students
           usr.instructors=ins
         
           usr.save()
           stud =Course.objects.values()
           student_data =list(stud)
           return JsonResponse({'status':'Save',
           'course_data':student_data})
     else:
           return JsonResponse({'status':0})

def list_coursedata(request):
    if request.method == "GET":
          context ={'data_read':Course.objects.all()}

          print(context)
          student_data =serializers.serialize('json',Course.objects.all())
          print (student_data)
          return JsonResponse(student_data,safe=False)
    return JsonResponse({'message':'wrongvalidation'})

def delete_data(request):
     if request.method == "POST":
      id=request.POST.get('id');
      pi=Course.objects.get(pk=id)
      pi.delete();
      return JsonResponse({'status':1})
     else:
      return JsonResponse({'status':0})

def add_course(request):
    subjectss=Instructor.objects.all()
    context = {'subjectss':subjectss}
    return render (request,'addcourse.html',context)

def instruct_list(request):
    csw = {'subjects':Instructor.objects.all()}
    print (csw)
    return render(request,csw)

def edit_data(request):
     if request.method == "POST":
      id=request.POST.get('sid')
      pi=Course.objects.get(pk=id)
      course_data={"id":pi.id,"course_code":pi.course_code,"course_name":pi.course_name,"max_numb_students":pi.max_numb_students,"instructors":pi.instructors.id}
      return JsonResponse(course_data)

def add_department(request):
    return render (request,'adddepartment.html')

def all_department(request):
    return render (request,'alldepartment.html')

def all_room(request):
    return render (request,'allroom.html')

def add_room(request):
    return render (request,'addroom.html')

def all_time(request):
    return render (request,'alltime.html')

def add_time(request):
    return render (request,'addtime.html')

def all_section(request):
    return render (request,'allsection.html')

def add_section(request):
    return render (request,'addsection.html')
    profile
def all_profile(request):
    return render (request,'profile.html')

def all_change(request):
    return render (request,'change.html')

def all_dashboard(request):
    return render (request,'dashboard.html')


    
def signup(request):
    return render(request,'signup.html') 
    

def course(request):
    return render(request,'course.html') 
    
def about(request):
    return render(request,'about.html') 

def single(request):
    return render(request,'single.html') 

def contact(request):
    return render(request,'contact.html') 

def basepage(request):
    return render(request,'base.html') 

def teacher(request):
    return render(request,'teacher.html')
def homepage(request):
    return render(request,'homepage.html')
def homepage(request):
    return render (request,'homepage.html')