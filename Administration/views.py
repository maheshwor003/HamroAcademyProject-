from django.shortcuts import render, redirect

from TeacherAndStudent.models import Departments
from .models import Course, Instructor
from django.http import JsonResponse
from django.core import serializers
from .models import *
from .forms import Room
from TeacherAndStudent.models import *
from django.contrib.auth import logout
from .forms import *
# Create your views here.




def adminpage(request):
    return render (request,'adminpage.html')


def teacher(request):
    return render(request,'teacherpage.html')


def student(request):
    return render(request,'studentpage.html')

def logout_out(request):
    logout(request)
    return redirect('homepage')

def base(request):
    return render (request,'dashboard.html')
def add_teacher(request):
    form = InstructorForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('addteacher')
        else:
            print('Invalid')
    context = {
        'form': form,
    }
    return render(request, 'add-teacher.html', context)
def all_teacher(request):
    subjects = Instructor.objects.all()
    dataread=Instructor.objects.all()
    context = {'teachers_view': subjects,'data_read':dataread}
    return render(request, 'all-teacher.html', context)
    
def delete_instructor(request, uid):
    inss = Instructor.objects.filter(uid=uid)
    if request.method == 'POST':
        inss.delete()
        return redirect('allteacher')
    

    
def all_course(request):
   
    subjects=Courses.objects.all()
    dataread=Course.objects.all()
    context = {'subjects':subjects,'data_read':dataread}
    return render (request,'allcourse.html',context)

def delete_course(request, pk):
    crs = Course.objects.filter(pk=pk)
    crss = Courses.objects.filter(pk=pk)
    if request.method == 'POST':
        crs.delete()
        crss.delete()
        return redirect('allcourse')

def delete_room(request, r_number):
    room = Room.objects.filter(r_number=r_number)
    if request.method == 'POST':
        room.delete()
        return redirect('allroom')



def delete_section(request, section_id):
    section = Section.objects.filter(section_id=section_id)
    if request.method == 'POST':
        section.delete()
        return redirect('allsection')

def delete_time(request, r_number):
    room = Room.objects.filter(r_number=r_number)
    if request.method == 'POST':
        room.delete()
        return redirect('allroom')

def delete_department(request, id):
    department = Department.objects.filter(id=id)
    if request.method == 'POST':
        department.delete()
        return redirect('alldepartment')


def savecourse_data(request):
     if request.method == "POST":
           
           course_number= request.POST.get('course_number')
           course_name= request.POST['name']
           description=request.POST['description']
           status=request.POST['status']
           depart= request.POST['department']
           ins=Departments.objects.get(id=depart)
         
           usr= Courses(course_number=course_number,name=course_name,description=description,status=status,department=ins)
           print(usr)
           usr.save()
           stud =Courses.objects.values()
           student_data =list(stud)
           return JsonResponse({'status':'Save',
           'course_data':student_data})
     else:
           return JsonResponse({'status':0})

def updatedepartment_data(request,id):
    if request.method== 'POST':
      dept = Department.objects.get(pk=id)
      form = DepartmentForm(request.POST or None, instance=dept)
      if form.is_valid():
        form.save()
    else:
        dept = Department.objects.get(pk=id)
        form = DepartmentForm(instance=dept)
          
    return render(request,'update.html' ,{'form':form})


def updatecourse_data(request,course_number):
    if request.method== 'POST':
      course = Course.objects.get(course_number=course_number)
      form = CourseForm(request.POST or None, instance=course)
      if form.is_valid():
        form.save()
    else:
        course = Course.objects.get(course_number=course_number)
        form = CourseForm(instance=course)
          
    return render(request,'update.html',{'form':form})



def updateinstructor_data(request,uid):
    if request.method== 'POST':
      ins = Instructor.objects.get(uid=uid)
      form = InstructorForm(request.POST or None, instance=ins)
      if form.is_valid():
        form.save()
    else:
        ins = Instructor.objects.get(uid=uid)
        form = InstructorForm(instance=ins)
          
    return render(request,'update.html' ,{'form':form})    

def updatesection_data(request,section_id):
    if request.method== 'POST':
      sec = Section.objects.get(section_id=section_id)
      form = SectionForm(request.POST or None, instance=sec)
      if form.is_valid():
        form.save()
    else:
        sec = Section.objects.get(section_id=section_id)
        form = SectionForm(instance=sec)
          
    return render(request,'update.html' ,{'form':form}) 


def update_data(request,id):
    if request.method== 'POST':
      roomno = Room.objects.get(r_number=id)
      form = RoomForm(request.POST or None, instance=roomno)
      if form.is_valid():
        form.save()
    else:
        roomno = Room.objects.get(r_number=id)
        form = RoomForm(instance=roomno)
          
    return render(request,'update.html' ,{'form':form})


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
      id=request.POST.get('course_name');
      id=request.POST.get('ins');
      id=request.POST.get('room');
      pi=Course.objects.get(pk=id)
      pi=Instructor.objects.get(pk=id)
      pi=Room.objects.get(r_number=id)
      pi.delete();
      return JsonResponse({'status':1})
     else:
      return JsonResponse({'status':0})


# def add_course(request):
#     subjectss=Instructor.objects.all()
#     context = {'subjectss':subjectss}
#     return render (request,'addcourse.html',context)


def add_course(request):
    listdepartment=Departments.objects.all()
    form = CourseForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('addcourse')
        else:
            print('Invalid')
    context = {
        'form': form,'departments':listdepartment
    }
    return render(request, 'addcourse.html', context)

def add_instructor(request):
    form = InstructorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addinstructor')
    context = {
        'form': form
    }
    return render(request, 'add-teacher.html', context)



def instruct_list(request):
    csw = {'subjects':Instructor.objects.all()}
    print (csw)
    return render(request,csw)

def add_section(request):
    form = SectionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addsection')
    context = {
        'form': form
    }
    return render(request, 'addsection.html', context)


def all_section(request):

    subjects = Section.objects.all()
    context = {'sections': subjects}
    return render(request, 'allsection.html', context)

def edit_data(request):
     if request.method == "POST":
      id=request.POST.get('sid')
      pi=Course.objects.get(pk=id)
      course_data={"id":pi.id,"course_code":pi.course_code,"course_name":pi.course_name,"max_numb_students":pi.max_numb_students,"instructors":pi.instructors.id}
      return JsonResponse(course_data)

def add_department(request):

    form = DepartmentForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('adddepartment')
        else:
            print('Invalid')
    context = {
        'form': form
    }

    return render(request, 'adddepartment.html', context)


def all_department(request):
    subjects = Department.objects.all()

    context = {'department_list': subjects}
    return render(request, 'alldepartment.html', context)

def all_room(request):

    subjects = Room.objects.all()
    context = {'Room_view': subjects}

    return render(request, 'allroom.html', context)


def add_room(request):
    form = RoomForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('addroom')
        else:
            print('Invalid')
    context = {
        'form': form,
    }
    return render(request, 'addroom.html', context)

def add_time(request):
    form = MeetingTimeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addtime')
        else:
            print('Invalid')
    context = {
        'form': form,
    }
    return render(request, 'addtime.html', context)

 
def all_profile(request):
    return render (request,'profile.html')

def all_change(request):
    return render (request,'change.html')

def all_dashboard(request):

    courses = Course.objects.count()
    teacher = Instructor.objects.count()
    context = {'courses': courses,'teacher':teacher}
    return render (request,'dashboard.html',context)

class Data:
    def __init__(self):
        self._rooms = Room.objects.all()
        self._meetingTimes = MeetingTime.objects.all()
        self._instructors = Instructor.objects.all()
        self._courses = Course.objects.all()
        self._depts = Department.objects.all()

    def get_rooms(self): return self._rooms

    def get_instructors(self): return self._instructors

    def get_courses(self): return self._courses

    def get_depts(self): return self._depts

    def get_meetingTimes(self): return self._meetingTimes




class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numberOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self): return self._numberOfConflicts

    def get_fitness(self):
        if self._isFitnessChanged:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        sections = Section.objects.all()
        for section in sections:
            dept = section.department
            n = section.num_class_in_week
            if n <= len(MeetingTime.objects.all()):
                courses = dept.courses.all()
                for course in courses:
                    for i in range(n // len(courses)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept, section.section_id, course)
                        self._classNumb += 1
                        newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(MeetingTime.objects.all()))])
                        newClass.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                        newClass.set_instructor(crs_inst[rnd.randrange(0, len(crs_inst))])
                        self._classes.append(newClass)
            else:
                n = len(MeetingTime.objects.all())
                courses = dept.courses.all()
                for course in courses:
                    for i in range(n // len(courses)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept, section.section_id, course)
                        self._classNumb += 1
                        newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(MeetingTime.objects.all()))])
                        newClass.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                        newClass.set_instructor(crs_inst[rnd.randrange(0, len(crs_inst))])
                        self._classes.append(newClass)

        return self

        
    def calculate_fitness(self):
        self._numberOfConflicts = 0
        classes = self.get_classes()
        for i in range(len(classes)):
            if classes[i].room.seating_capacity < int(classes[i].course.max_numb_students):
                self._numberOfConflicts += 1
            for j in range(len(classes)):
                if j >= i:
                    if (classes[i].meeting_time == classes[j].meeting_time) and \
                            (classes[i].section_id != classes[j].section_id) and (classes[i].section == classes[j].section):
                        if classes[i].room == classes[j].room:
                            self._numberOfConflicts += 1
                        if classes[i].instructor == classes[j].instructor:
                            self._numberOfConflicts += 1
        return 1 / (1.0 * self._numberOfConflicts + 1)





class Class:
    def __init__(self, id, dept, section, course):
        self.section_id = id
        self.department = dept
        self.course = course
        self.instructor = None
        self.meeting_time = None
        self.room = None
        self.section = section

    def get_id(self): return self.section_id

    def get_dept(self): return self.department

    def get_course(self): return self.course

    def get_instructor(self): return self.instructor

    def get_meetingTime(self): return self.meeting_time

    def get_room(self): return self.room

    def set_instructor(self, instructor): self.instructor = instructor

    def set_meetingTime(self, meetingTime): self.meeting_time = meetingTime

    def set_room(self, room): self.room = room

data = Data()

class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if rnd.random() > 0.5:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(len(mutateSchedule.get_classes())):
            if MUTATION_RATE > rnd.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop



class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = [Schedule().initialize() for i in range(size)]

    def get_schedules(self):
        return self._schedules

def context_manager(schedule):
    classes = schedule.get_classes()
    context = []
    cls = {}
    for i in range(len(classes)):
        cls["section"] = classes[i].section_id
        cls['dept'] = classes[i].department.dept_name
        cls['course'] = f'{classes[i].course.course_name} ({classes[i].course.course_number}, ' \
                        f'{classes[i].course.max_numb_students}'
        cls['room'] = f'{classes[i].room.r_number} ({classes[i].room.seating_capacity})'
        cls['instructor'] = f'{classes[i].instructor.name} ({classes[i].instructor.uid})'
        cls['meeting_time'] = [classes[i].meeting_time.pid, classes[i].meeting_time.day, classes[i].meeting_time.time]
        context.append(cls)
        print(context)
    return context


def routinegeneration(request):
    schedule = []
    population = Population(POPULATION_SIZE)
    generation_num = 0
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    geneticAlgorithm = GeneticAlgorithm()
    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_num += 1
        print('\n> Generation #' + str(generation_num))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        schedule = population.get_schedules()[0].get_classes()
      
    return render(request, 'routinegeneration.html', {'schedule': schedule, 'sections': Section.objects.all(),
                                              'times': MeetingTime.objects.all()})



def teacherroutinegeneration(request):
    schedule = []
    population = Population(POPULATION_SIZE)
    generation_num = 0
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    geneticAlgorithm = GeneticAlgorithm()
    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_num += 1
        print('\n> Generation #' + str(generation_num))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        schedule = population.get_schedules()[0].get_classes()
      
    return render(request, 'teacherroutine.html', {'schedule': schedule, 'sections': Section.objects.all(),
                                              'times': MeetingTime.objects.all()})





def alltime(request):
    return render(request,'alltime.html') 
    
    
def signup(request):
    return render(request,'signup.html') 
    

def course(request):
    return render(request,'course.html',{'navbar':'course'}) 
    
def about(request):
    return render(request,'about.html',{'navbar':'about'}) 

def single(request):
    return render(request,'single.html',{'navbar':'single'}) 

def contact(request):
    return render(request,'contact.html',{'navbar':'contact'}) 

def basepage(request):
    csw = {'subjects':Instructor.objects.all().count()}
    print (csw)
    return render(request,'base.html') 

def teacher(request):
    return render(request,'teacher.html',{'navbar':'teacher'})
def homepage(request):
    return render(request,'homepage.html',{'navbar':'homepage'})


# def attendance(request, stud_id):
#     stud = Student.objects.get(USN=stud_id)
#     ass_list = Assign.objects.filter(class_id_id=stud.class_id)
#     att_list = []
#     for ass in ass_list:
#         try:
#             a = AttendanceTotal.objects.get(student=stud, course=ass.course)
#         except AttendanceTotal.DoesNotExist:
#             a = AttendanceTotal(student=stud, course=ass.course)
#             a.save()
#         att_list.append(a)
#     return render(request, 'attendance.html', {'att_list': att_list})


def studentnavbar(request):
    return render (request,'studentnavbar.html')

def studentprofile(request):
    return render (request,'studentprofile.html')

def studentattendence(request,stud_id):
      stud = Student.objects.get(USN=stud_id)
      ass_list = Assign.objects.filter(class_id_id=stud.class_id)
      att_list = []
      for ass in ass_list:
          try:
              a = AttendanceTotal.objects.get(student=stud, course=ass.course)
          except AttendanceTotal.DoesNotExist:
              a = AttendanceTotal(student=stud, course=ass.course)
              a.save()
          att_list.append(a)
      return render(request, 'attendance.html', {'att_list': att_list})


def marks_list(request, stud_id):
    stud = Student.objects.get(USN=stud_id, )
    ass_list = Assign.objects.filter(class_id_id=stud.class_id)
    sc_list = []
    for ass in ass_list:
        try:
            sc = StudentCourse.objects.get(student=stud, course=ass.course)
        except StudentCourse.DoesNotExist:
            sc = StudentCourse(student=stud, course=ass.course)
            sc.save()
            sc.marks_set.create(type='I', name='Internal test 1')
            sc.marks_set.create(type='I', name='Internal test 2')
            sc.marks_set.create(type='I', name='Internal test 3')
            sc.marks_set.create(type='E', name='Event 1')
            sc.marks_set.create(type='E', name='Event 2')
            sc.marks_set.create(type='S', name='Semester End Exam')
        sc_list.append(sc)

    return render(request, 'result.html', {'sc_list': sc_list})

# # def attendance(request, stud_id):
# #     stud = Student.objects.get(USN=stud_id)
# #     ass_list = Assign.objects.filter(class_id_id=stud.class_id)
# #     att_list = []
# #     for ass in ass_list:
# #         try:
# #             a = AttendanceTotal.objects.get(student=stud, course=ass.course)
# #         except AttendanceTotal.DoesNotExist:
# #             a = AttendanceTotal(student=stud, course=ass.course)
# #             a.save()
# #         att_list.append(a)
# #     return render(request, 'attendance.html', {'att_list': att_list})


# def studentattendence(request):
#      return render (request,'attendence.html')

def studentpage(request):
    return render (request,'studentpage.html')

def result(request):
    return render (request,'result.html')


    
def teachernavbar(request):
    return render (request,'teachernavbar.html')
def t_result(request):
    return render (request,'t_result.html')
def t_attendence(request):
    return render (request,'t_attendence.html')
def teacherprofile(request):
    return render (request,'teacherprofile.html')
def teacherdashboard(request):
    return render (request,'teacherdashboard.html')
def routine(request):
    return render (request,'routine.html')