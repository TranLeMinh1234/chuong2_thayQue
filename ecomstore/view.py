
from django.http import HttpResponse
from django.shortcuts import render

from django.template import Context


def catalog(request): 
 my_context = Context({ 'site_name': 'Modern Musician' }) 
 return render(request,'catalog.html', { 'site_name': 'sss Musician' })  