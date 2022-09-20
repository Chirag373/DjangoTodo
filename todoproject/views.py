from django.shortcuts import redirect, render
from .models import *
import datetime as dt
# Create your views here.
def index(request):
    return render(request,'todoproject/index.html')

def insert_data(request):
    List = request.POST['search-box']
    D = dt.datetime.now()

    newuser = Todolist.objects.create(Content = List, Publish_date = D)

    return redirect('showPage')

def ShowPage(request):
    all_data = Todolist.objects.all()
    # print(all_data)
    return render(request,"todoproject/Show.html",{'key1':all_data})

def EditPage(request,pk):
    data = Todolist.objects.get(id=pk)
    return render(request, "todoproject/Edit.html",{'key2':data})

def Update(request,pk):
    udata = Todolist.objects.get(id=pk)
    udata.Content = request.POST['search-box']
    udata.save()
    return redirect('showPage')

def deletedata(request,pk):
    ddata = Todolist.objects.get(id=pk)
    ddata.delete()
    return redirect('showPage')