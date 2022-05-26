from django.shortcuts import render
from .models import Student
from .serialiser import StudentSerialiser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
def allStudent(request):
    s = Student.objects.all()
    serialiser = StudentSerialiser(s, many=True)
    json_data = JSONRenderer().render(serialiser.data)
    return HttpResponse(json_data, content_type = 'application/json')

def student(request, slug):
    # it will show particular student data whose slug is given
    s = Student.objects.get(id=slug)
    # it converted the complex model into python
    serialiser = StudentSerialiser(s)
    # it converted the python data into json data 
    json_data = JSONRenderer().render(serialiser.data)

    return HttpResponse(json_data, content_type = 'application/json')