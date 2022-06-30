from django.shortcuts import render
from rest_framework import generics 
from .models import Student 
from .serialisers import StudentSerialser

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialser

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialser
