"""
URL configuration for pot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from pot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'), 
    path('about/', views.aboutUs, name='aboutus'),
    path('contact/', views.contactUs, name='contact'),
    path('project/', views.project, name='project'),
    path('service/', views.service, name='service'),
    path('gallary', views.gallary, name='gallary'),
    path('socialmedia', views.socalmedia, name='socialmedia'),
    path('workexpe', views.workexperience, name='workexperience'),

]
