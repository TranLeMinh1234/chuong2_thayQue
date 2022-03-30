from django.shortcuts import render 

def booklist(request): 
 return render(request,"demo/BookList.html")

def home(request): 
 return render(request,"demo/index.html")