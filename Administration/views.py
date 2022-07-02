from django.shortcuts import render

# Create your views here.




def adminpage(request):
    return render (request,'adminpage.html')





def teacher(request):
    return render(request,'teacherpage.html')


def student(request):
    return render(request,'studentpage.html')