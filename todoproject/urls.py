from importlib.resources import path
from pathlib import Path
from django.contrib import admin

from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.index,name="Index"),
   path("insertdata/",views.insert_data,name="insertdata"),
   path("showPage/",views.ShowPage,name="showPage"),
   path("EditPage/<int:pk>",views.EditPage,name="EditPage"),
   path("update/<int:pk>",views.Update,name="update"),
   path("Delete/<int:pk>",views.deletedata,name="Delete"),
]
