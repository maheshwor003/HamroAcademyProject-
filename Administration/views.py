from django.shortcuts import render

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
    
def all_course(request):
    return render (request,'allcourse.html')

def add_course(request):
    return render (request,'addcourse.html')

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
   
def teacher(request):
    return render(request,'teacher.html')
def homepage(request):
    return render(request,'homepage.html')
def homepage(request):
    return render (request,'homepage.html')