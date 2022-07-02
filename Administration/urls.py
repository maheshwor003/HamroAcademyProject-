
from django.urls import path
from  Administration import views
urlpatterns = [

    
    path('adminpage/', views.adminpage, name='adminpage'),
    path('teacherpage/', views.teacher, name='teacherpage'),
    path('studentpage/', views.student, name='studentpage'),
]
