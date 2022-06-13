from urllib import response
from api.serialiser import TodoSerialiser
from .models import Todo 
from .serialiser import TodoSerialiser
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

'''
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

@api_view(['POST'])
def update_view(request, pk):
    try:
        task = Todo.objects.get(id = pk)
    except:
        return Response('No data found')
    s = TodoSerialiser(instance=task, data=request.data)
    if s.is_valid():
        s.save()
    return Response(s.data)

@api_view(['DELETE'])
def delete_view(request, pk):
    try:
        task = Todo.objects.get(id = pk)
    except:
        return Response('No data found')
    task.delete()
    return Response('Item deleted')
'''

# to read 
'''
class TodoClassBasedView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                todo = Todo.objects.get(id = pk)
            except:
                return Response('No data found', status=status.HTTP_404_NOT_FOUND)
            s = TodoSerialiser(todo)
            return Response(s.data, status=status.HTTP_200_OK)
        todo = Todo.objects.all()
        s = TodoSerialiser(todo, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None, format=None):
        s = TodoSerialiser(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def put(self, request, pk=None, format=None):
        try:
            task = Todo.objects.get(id = pk)
        except:
            return Response('No data found')
        s = TodoSerialiser(task, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk=None, format=None):
        try:
            task = Todo.objects.get(id = pk)
        except:
            return Response('No data found', status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response('Deleted!', status=status.HTTP_200_OK)
'''

'''
class TodoMixinList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
    ):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class TodoMixinDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
    ):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''

class TodoGenericList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser

class TodoGenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser