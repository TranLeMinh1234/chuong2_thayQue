from pydoc import describe
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from itsdangerous import Serializer
from preview.models import Book, Shoes 
from django.core.files.storage import FileSystemStorage
from django.core import serializers

def booklist(request): 
 return render(request,"demo/BookList.html")

def home(request): 
 return render(request,"demo/index.html")

class ObjectToDisplay:
    properties = []
    
def list(request,productName):
    model = getModelByName(productName)
    listField = []
    listObject = []  
    listFieldType = []
      
    for field in model._meta.fields:
        cloneObjectFieldType = field.__dict__ 
        cloneObjectFieldType['type'] = field.get_internal_type()
        listFieldType.append(cloneObjectFieldType)
        listField.append(field.name)
    for object in model.objects.all():
        cloneObject = object.__dict__
        cloneObject['properties'] = []
        for field in model._meta.fields:
            cloneObject['properties'].append(cloneObject[field.name])
        listObject.append(cloneObject)
        
    template_name = 'demo/BookList.html'
    obj = {
      'listObject': listObject,
      'listField': listField,
      'listFieldType': listFieldType,
      'modelName': model._meta.object_name
    }
    return render(request, template_name, obj)

def add(request,productName):
    model = getModelByName(productName)
    data_dic = {}
    for field in model._meta.fields:
        if field.name != "image" and field.name != "id":
            data_dic[field.name] =  request.POST[field.name]
            
    file = request.FILES['file']
    
    fs = FileSystemStorage(location="preview/static/preview/img") #defaults to   MEDIA_ROOT  
    filename = fs.save(file.name, file)
    file_url = '/preview/img' + fs.url(filename)
    
    data_dic['image'] =  file_url
    modelSave = model(**data_dic)
    modelSave.save()
    return redirect('list',productName)

def delete(request, productName, idRecord):
    model = getModelByName(productName)
    instance = model.objects.get(id=idRecord)
    instance.delete()
    return redirect('list',productName)

def update(request, productName, idRecord):
    model = getModelByName(productName)
    data_dic = {}
    for field in model._meta.fields:
        if field.name != "image" and field.name != "id":
            data_dic[field.name] =  request.POST[field.name]
        elif field.name == "id":
            data_dic[field.name] =  idRecord
            
    file = request.FILES['file']
    
    fs = FileSystemStorage(location="preview/static/preview/img") #defaults to   MEDIA_ROOT  
    filename = fs.save(file.name, file)
    file_url = '/preview/img' + fs.url(filename)
    
    data_dic['image'] =  file_url
    modelSave = model(**data_dic)
    modelSave.save()
    return redirect('list',productName)

def getRecord(request, productName ,idRecord):
    model = getModelByName(productName)
    modelInstace = model.objects.filter(id=idRecord)
    data = serializers.serialize('json', modelInstace)
    return HttpResponse(data, content_type="application/json")

def getModelByName(productName):
    if productName == "Book":
        return Book
    elif productName == "Shoes":
        return Shoes
