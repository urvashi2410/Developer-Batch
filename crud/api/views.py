from api.serialiser import TodoSerialiser
from .models import Todo 
from .serialiser import TodoSerialiser
from rest_framework.response import Response 
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def read_view(request):
    todos = Todo.objects.all()
    s = TodoSerialiser(todos, many=True)
    return Response(s.data)

@api_view(['GET'])
def read_view_particular(request, pk):
    try:
        todo = Todo.objects.get(id = pk)
    except:
        return Response('No data found')
    s = TodoSerialiser(todo, many=False)
    return Response(s.data)

@api_view(['POST'])
def create_view(request):
    s = TodoSerialiser(data=request.data)
    if s.is_valid():
        s.save()
    return Response(s.data)

    