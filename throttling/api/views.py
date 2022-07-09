from rest_framework import generics
from .models import Todo
from .serialisers import TodoSerialiser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

# Create your views here.
class SnippetList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    throttle_scope = 'list'

class SnippetRetrieve(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    throttle_scope = 'get_one'

class SnippetUpdate(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    throttle_scope = 'update'

class SnippetCreate(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    throttle_scope = 'create'

class SnippetDestroy(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    throttle_scope = 'destroy'
