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

from preview.views import (home,booklist,listBook,addBook,deleteBook,updateBook,getRecord)

from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', home, name='Home'),
    path('book-list', listBook, name='listBook'),
    path('addBook', addBook, name='addBook'),
    path('deleteBook/<int:idRecord>', deleteBook, name='deleteBook'),
    path('updateBook/<int:idRecord>', updateBook, name='updateBook'),
    path('getRecord/<int:idRecord>', getRecord, name='getRecord'),
]
