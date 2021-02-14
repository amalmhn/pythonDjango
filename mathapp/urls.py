"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path , include
from .views import get_addition_page,calculate,get_sub_page,substraction,get_mul_page,multiplication,\
    get_div_page,division

urlpatterns = [
    path('add',get_addition_page,name='getadd'),
    path('calc',calculate,name='calc'),
    path('sub',get_sub_page,name='sub'),
    path('substraction',substraction,name='substraction'),
    path('mul',get_mul_page,name='mul'),
    path('multiplication',multiplication,name='multiplication'),
    path('div',get_div_page,name='div'),
    path('division',division,name='division')


]
