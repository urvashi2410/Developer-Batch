from django.shortcuts import render
from rest_framework import generics 
from .models import Student 
from .serialisers import StudentSerialser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialser
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialser
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
