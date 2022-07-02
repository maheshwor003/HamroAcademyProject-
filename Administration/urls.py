
from django.urls import path
from  Administration import views
urlpatterns = [

    
    path('adminpage/', views.adminpage, name='adminpage'),
    path('teacherpage/', views.teacher, name='teacherpage'),
    path('studentpage/', views.student, name='studentpage'),
   
   
    path('allteacher/',views.all_teacher,name='allteacher'),
    path('addteacher/',views.add_teacher,name='addteacher'),
    path('addcourse/',views.add_course,name='addcourse'),
    path('allcourse/',views.all_course,name='allcourse'),
    path('alldepartment/',views.all_department,name='alldepartment'),
    path('adddepartment/',views.add_department,name='adddepartment'),
    path('allroom/',views.all_room,name='allroom'),
    path('addroom/',views.add_room,name='addroom'),
    path('alltime/',views.all_time,name='alltime'),
    path('addtime/',views.add_time,name='addtime'),
    path('allsection/',views.all_section,name='allsection'),
    path('addsection/',views.add_section,name='addsection'),
    path('change/',views.all_change,name='change'),
    path('profile/',views.all_profile,name='profile'),
    path('dashboard/',views.all_dashboard,name='dashboard'),

    path('homepage/', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('teacher/', views.teacher, name='teacher'),
    path('single/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
]
