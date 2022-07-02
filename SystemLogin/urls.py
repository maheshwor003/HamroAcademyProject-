
from django.urls import path
from  SystemLogin import views
urlpatterns = [
 
    path('', views.home, name='home'),
]
