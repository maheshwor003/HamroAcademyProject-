
from django.urls import path
from  Administration import views
urlpatterns = [

    
    path('adminpage/', views.adminpage, name='adminpage'),
    path('teacherpage/', views.teacher, name='teacherpage'),
    path('studentpage/', views.student, name='studentpage'),
    path('logout/', views.logout_out, name='logout'),
   
   
    path('allteacher/',views.all_teacher,name='allteacher'),
    path('addteacher/',views.add_teacher,name='addteacher'),
    path('addcourse/',views.add_course,name='addcourse'),
    path('allcourse/',views.all_course,name='allcourse'),
    path('listcourse/',views.list_coursedata,name = "listcoursedata"),
    path('alldepartment/',views.all_department,name='alldepartment'),
    path('adddepartment/',views.add_department,name='adddepartment'),
    path('allroom/',views.all_room,name='allroom'),
    path('addroom/',views.add_room,name='addroom'),
    path('alltime/',views.alltime,name='alltime'),
    path('addtime/',views.add_time,name='addtime'),
    path('allsection/',views.all_section,name='allsection'),
    path('addsection/',views.add_section,name='addsection'),
    path('change/',views.all_change,name='change'),
    path('profile/',views.all_profile,name='profile'),
    path('dashboard/',views.all_dashboard,name='dashboard'),
    path('edit/',views.edit_data,name = "edit"),
    path('getinstructors/',views.instruct_list,name = "getinstructors"),
    path('homepage/', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('updatecourse/<str:id>/', views.updatecourse_data, name='updatecourse'),
    path('teacher/', views.teacher, name='teacher'),
    path('single/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
    path('base/', views.basepage, name='base'),
    path('savecourse/',views.savecourse_data,name='savecourse'),
    path('delete_course/<str:pk>/', views.delete_course, name='deletecourse'),
    path('delete/',views.delete_data,name = "delete"),
    path('attendence/',views.attendence,name='attendence'),
    path('result/',views.result,name='result'),
    path('studentprofile/', views.studentprofile, name='studentprofile'),
    

]
