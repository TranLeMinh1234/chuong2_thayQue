from pydoc import describe
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from itsdangerous import Serializer
from preview.models import Book 
from django.core.files.storage import FileSystemStorage
from django.core import serializers

def booklist(request): 
 return render(request,"demo/BookList.html")

def home(request): 
 return render(request,"demo/index.html")

class ObjectToDisplay:
    properties = []
    
def listBook(request):
    model = Book
    listField = []
    listObject = []  
      
    for field in model._meta.fields:
        listField.append(field.name)
    
    for object in Book.objects.all():
        cloneObject = object.__dict__
        cloneObject['properties'] = []
        for field in model._meta.fields:
            cloneObject['properties'].append(cloneObject[field.name])
        listObject.append(cloneObject)
        
    template_name = 'demo/BookList.html'
    obj = {
      'listObject': listObject,
      'listField': listField
    }
    return render(request, template_name, obj)

def addBook(request):
    name = request.POST['name']
    des = request.POST['description']
    price = request.POST['price']
    file = request.FILES['file']
    
    fs = FileSystemStorage(location="preview/static/preview/img") #defaults to   MEDIA_ROOT  
    filename = fs.save(file.name, file)
    file_url = '/preview/img' + fs.url(filename)
    
    book = Book(name=name,description=des,price=price,image=file_url)
    book.save()
    return redirect('listBook')

def deleteBook(request, idRecord):
    instance = Book.objects.get(id=idRecord)
    instance.delete()
    return redirect('listBook')

def updateBook(request, idRecord):
    name = request.POST['name']
    des = request.POST['description']
    price = request.POST['price']
    file = request.FILES['file']
    
    if(file!=None):
        fs = FileSystemStorage(location="preview/static/preview/img") #defaults to   MEDIA_ROOT  
        filename = fs.save(file.name, file)
        file_url = '/preview/img' + fs.url(filename)
    
    book = Book(id=idRecord,name=name,description=des,price=price,image=file_url)
    book.save()
    return redirect('listBook')

def getRecord(request, idRecord):
    book = Book.objects.filter(id=idRecord)
    data = serializers.serialize('json', book)
    return HttpResponse(data, content_type="application/json")
