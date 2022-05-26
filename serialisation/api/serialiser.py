from ftplib import MAXLINE
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Student 

class StudentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ['name', 'rollNo', 'city']
