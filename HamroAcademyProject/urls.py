"""HamroAcademyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from  SystemLogin import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('SystemLogin/', include('SystemLogin.urls')),
    path('Administration/', include('Administration.urls')),
    path('TeacherAndStudent/', include('TeacherAndStudent.urls')),
    

    # path('accounts/login/', auth_views.LoginView.as_view(template_name='info/login.html'), name='login'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
