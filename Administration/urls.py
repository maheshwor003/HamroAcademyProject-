
from django.urls import path
from Administration import views
urlpatterns = [


    path('adminpage/', views.adminpage, name='adminpage'),
    path('teacherpage/', views.teacher, name='teacherpage'),
    path('studentpage/', views.student, name='studentpage'),
    path('logout/', views.logout_out, name='logout'),
    path('allteacher/',views.all_teacher,name='allteacher'),
    path('addteacher/',views.add_teacher,name='addteacher'),
    path('allstudent/',views.all_student,name='allstudent'),
    path('addstudent/',views.add_student,name='addstudent'),
    path('addcourse/',views.add_course,name='addcourse'),
    path('allcourse/',views.all_course,name='allcourse'),
    path('listcourse/',views.list_coursedata,name = "listcoursedata"),
    path('alldepartment/',views.all_department,name='alldepartment'),
    path('adddepartment/',views.add_department,name='adddepartment'),
    path('savedepartment/',views.savedepartment,name='savedepartment'),
    path('allroom/',views.all_room,name='allroom'),
    path('addroom/',views.add_room,name='addroom'),
    
    
    path('addtime/', views.add_time, name='addtime'),
    path('allsection/', views.all_section, name='allsection'),
    path('addsection/', views.add_section, name='addsection'),
    path('change/', views.all_change, name='change'),
    path('profile/', views.all_profile, name='profile'),
    path('dashboard/', views.all_dashboard, name='dashboard'),
    path('edit/', views.edit_data, name="edit"),
    path('getinstructors/', views.instruct_list, name="getinstructors"),
    
    
   
    path('updatecourse/<str:course_number>',
         views.updatecourse_data, name='updatecourse'),
    path('updateinstructor/<str:uid>',
         views.updateinstructor_data, name='updateinstructor'),
    path('updatedepartment/<str:id>',
         views.updatedepartment_data, name='updatedepartment'),
    path('updatesection/<str:section_id>',
         views.updatesection_data, name="updatesection"),
    path('updatetime/<str:pid>',
         views.updatetime_data, name="updatetime"),
     path('updatestudent/<str:USN>',
         views.updatestudent_data, name='updatestudent'),
    path('update/<str:id>', views.update_data, name="updatedata"),
    path('addroutine/', views.addroutine, name='addroutine'),
    path('deleteroutine/', views.deleteroutine, name='deleteroutine'),
    path('saveroutine/', views.saveroutine, name='saveroutine'),
    path('base/', views.basepage, name='base'),
    path('savecourse/', views.savecourse_data, name='savecourse'),
    path('delete_course/<str:pk>/', views.delete_course, name='deletecourse'),
    path('deleteinstructor/<str:pk>/',views.deleteinstructor, name='deleteinstructor'),
    path('delete_room/<str:r_number>/', views.delete_room, name='deleteroom'),
    path('delete_time/<str:pid>/', views.delete_time, name='deletetime'),
    path('delete_department',views.delete_department, name='delete_department'),
    path('deletedepartment/<str:dept_name>/', views.deletedepartment, name='deletedepartment'),



    path('delete_section/<str:section_id>/',
         views.delete_section, name='deletesection'),
     path('deletetudent/<str:USN>',
         views.deletestudent_data, name='deletestudent'),
    path('delete/', views.delete_data, name="delete"),
    path('student/<slug:stud_id>/marks_list/',
         views.marks_list, name='marks_list'),
    path('student/attendance/<slug:stud_id>/',
         views.studentattendence, name='attendance'),
    #path('attendance/', views.studentattendence, name='attendance'),
    path('result/', views.result, name='result'),
    path('teacherprofile/', views.teacherprofile, name='teacherprofile'),
    path('teacherdashboard/', views.teacherdashboard, name='teacherdashboard'),
    path('t_attendance/', views.t_attendence, name='t_attendence'),
    path('t_result/', views.t_result, name='t_result'),
    path('deleteteacher/',views.deleteteacher,name = "deleteteacher"),
    path('studentprofile/', views.studentprofile, name='studentprofile'),
    path('teachernavbar/', views.teachernavbar, name='teachernavbar'),
    path('t_attendence/', views.t_attendence, name='t_attendence'),
    path('t_result/', views.result, name='t_result'),
    path('teacherprofile/', views.teacherprofile, name='teacherprofile'),
    path('teacherdashboard/', views.teacherdashboard, name='teacherdashboard'),
    path('routinestudent/', views.routinegenerationstudent, name='routinestudent'),
    path('routineteacher/', views.routinegenerationteacher, name='routineteacher'),
    path('routine/', views.routine, name='routine'),
    path('alltime/', views.all_time, name='alltime'),
    path('saveteacher/', views.saveteacher, name='saveteacher'),
    path('savecoursedata/', views.savecoursedata, name='savecoursedata'),
    



]
