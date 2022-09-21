from django.shortcuts import render, redirect
from multiprocessing import context
from typing_extensions import Self
from django.shortcuts import render
from .models import Courses, Departments, Instructors, Rooms
from django.http import JsonResponse
from django.core import serializers
from. forms import *
# Create your views here.


def adminpage(request):
    return render(request, 'adminpage.html')


def teacher(request):
    return render(request, 'teacherpage.html')


def student(request):
    return render(request, 'studentpage.html')


def base(request):
    return render(request, 'dashboard.html')


def add_teacher(request):
    return render(request, 'add-teacher.html')


def all_teacher(request):
    teachers_view = Instructors.objects.all()
    context = {'teachers_view': teachers_view}
    return render(request, 'all-teacher.html', context)

# def all_course(request):
#     return render (request,'allcourse.html')


def all_course(request):
    subjects = Instructors.objects.all()
    dataread = Courses.objects.all()
    context = {'subjects': subjects, 'data_read': dataread}
    return render(request, 'allcourse.html', context)


def savecourse_data(request):
    if request.method == "POST":

        course_number = request.POST.get('course_number')
        course_name = request.POST['course_name']
        max_numb_students = request.POST['max_numb_students']
        instructors = request.POST['instructors']

        #old_subjects = Interest.objects.filter(pk=self.pk).first().subjects.all()
        # Instructors.objects.filter(id=Self.id).first().instructors.all()
        ins = Instructors.objects.filter(id=Self.id).first().instructors.all()

        usr = Courses(course_number=course_number, course_name=course_name,
                      max_numb_students=max_numb_students, instructors=ins)
        usr.save()
        print(usr)
        stud = Courses.objects.values()
        student_data = list(stud)
        return JsonResponse({'status': 'Save',
                             'course_data': student_data})
    else:
        return JsonResponse({'status': 0})


def saveteacher_data(request):
    if request.method == "POST":
        names = request.POST['nam']
        Addr = request.POST['Addre']
        teaimg = request.POST("timg")
        usr = Instructors(name=names, Address=Addr, image=teaimg)

        usr.save()
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def updatecourse_data(request, id):
    if request.method == "POST":
        course_code = request.POST.get('course_code')
        course_name = request.POST['course_name']
        max_numb_students = request.POST['max_numb_students']
        instructors = request.POST['instructors']
        ins = Instructors.objects.get(id=instructors)
        usr = Courses.objects.get(id=id)
        usr.course_code = course_code
        usr.course_name = course_name
        usr.max_numb_students = max_numb_students
        usr.instructors = ins

        usr.save()
        stud = Courses.objects.values()
        student_data = list(stud)
        return JsonResponse({'status': 'Save',
                             'course_data': student_data})
    else:
        return JsonResponse({'status': 0})


def list_coursedata(request):
    if request.method == "GET":
        context = {'data_read': Courses.objects.all()}

        print(context)
        student_data = serializers.serialize('json', Courses.objects.all())
        print(student_data)
        return JsonResponse(student_data, safe=False)
    return JsonResponse({'message': 'wrongvalidation'})


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('id')
        pi = Courses.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def add_course(request):
    subjectss = Instructors.objects.all()
    context = {'subjectss': subjectss}
    return render(request, 'addcourse.html', context)


def instruct_list(request):
    csw = {'subjects': Instructors.objects.all()}
    print(csw)
    return render(request, csw)


def editteacher_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = Instructors.objects.get(pk=id)
        instructor_data = {"id": pi.id, "name": pi.name, "Address": pi.Address}
        return JsonResponse(instructor_data)


def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = Courses.objects.get(pk=id)
        course_data = {"id": pi.id, "course_code": pi.course_code, "course_name": pi.course_name,
                       "max_numb_students": pi.max_numb_students, "instructors": pi.instructors.id}
        return JsonResponse(course_data)


def add_department(request):
    course_view = Courses.objects.all()
    context = {'coursess': course_view}
    return render(request, 'adddepartment.html', context)


def all_department(request):
    department_view = Courses.objects.all()
    dataread_department = Departments.objects.all()
    context = {'department_view': department_view,
               'data_read_department': dataread_department}

    print(dataread_department)
    return render(request, 'alldepartment.html', context)


def savedepartment_data(request):
    if request.method == "POST":
        dept_name = request.POST.get('dept_name')
        course = request.POST['coursess']
        ins = Courses.objects.get(id=course)
        usr = Departments(dept_name=dept_name, course=ins)
        usr.save()
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def all_room(request):
    Room_view = Rooms.objects.all()
    context = {'Room_view': Room_view}
    return render(request, 'allroom.html', context)


def add_room(request):

    return render(request, 'addroom.html')


def saveroom_data(request):
    if request.method == "POST":
        roomnumber = request.POST['roomnum']
        seatcapic = request.POST['seatcapi']
        usr = Rooms(room_number=roomnumber, seat_capacity=seatcapic)
        usr.save()
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def all_time(request):
    return render(request, 'alltime.html')


def add_time(request):
    return render(request, 'addtime.html')


def all_section(request):
    return render(request, 'allsection.html')


def add_section(request):
    return render(request, 'addsection.html')
    profile


def all_profile(request):
    return render(request, 'profile.html')


def all_change(request):
    return render(request, 'change.html')


def all_dashboard(request):
    return render(request, 'dashboard.html')


def signup(request):
    return render(request, 'signup.html')


def course(request):
    return render(request, 'course.html')


def about(request):
    return render(request, 'about.html')


def single(request):
    return render(request, 'single.html')


def contact(request):
    return render(request, 'contact.html')


def basepage(request):
    return render(request, 'base.html')


def teacher(request):
    return render(request, 'teacher.html')


def homepage(request):
    return render(request, 'homepage.html')


def homepage(request):
    return render(request, 'homepage.html')


def add_instructor(request):
    form = InstructorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addinstructor')
    context = {
        'form': form
    }
    return render(request, 'adns.html', context)
