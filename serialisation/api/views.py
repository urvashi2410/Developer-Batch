from .models import Student 
from .serialiser import StudentSerialiser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# fetching data of all the students 
def allStudent(request):
    s = Student.objects.all()
    serialsedData = StudentSerialiser(s, many=True)
    jsonData = JSONRenderer().render(serialsedData.data)
    return HttpResponse(jsonData, content_type = 'application/json')

# fetching data of a particular student with given slug 
def student(request, slug):
    s = Student.objects.get(id = slug) 
    # python me convert ho gya 
    serialisedData = StudentSerialiser(s)
    # python to json convert 
    jsonData = JSONRenderer().render(serialisedData.data)
    return HttpResponse(jsonData, content_type = 'application/json')
