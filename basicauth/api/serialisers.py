from .models import Student
from rest_framework import serializers

class StudentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = '__all__'