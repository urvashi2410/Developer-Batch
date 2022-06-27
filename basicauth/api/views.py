from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serialisers import StudentSerialiser
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [BasicAuthentication]

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [BasicAuthentication]