from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

#CRUD - Create, Read, Update, Delete
class CreateTodo(generics.CreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer

class ListToDo(generics.ListAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer

class DetailToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer