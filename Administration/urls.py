
from django.urls import path
from  Administration import views
urlpatterns = [
 
    path('adminpage/', views.adminpage, name='adminpage'),
]
