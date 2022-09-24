
from django.urls import path
from  SystemLogin import views
urlpatterns = [
 
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('navbar/', views.navbar, name='navbar'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('teacher/', views.teacher, name='teacher'),
    path('single/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
]
