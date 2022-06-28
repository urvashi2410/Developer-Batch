from django.shortcuts import render
from rest_framework import generics
from .models import Student 
from .serialisers import StudentSerialiser
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]