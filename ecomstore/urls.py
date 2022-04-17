"""ecomstore URL Configuration

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
from django.urls import path

from preview.views import (home,booklist,list,add,delete,update,getRecord)

from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', home, name='Home'),
    path('list/<str:productName>', list, name='list'),
    path('add/<str:productName>', add, name='add'),
    path('delete/<str:productName>/<int:idRecord>', delete, name='delete'),
    path('update/<str:productName>/<int:idRecord>', update, name='update'),
    path('getRecord/<str:productName>/<int:idRecord>', getRecord, name='getRecord'),
]
