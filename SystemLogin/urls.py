
from django.urls import path
from  SystemLogin import views
urlpatterns = [
 
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),

]
