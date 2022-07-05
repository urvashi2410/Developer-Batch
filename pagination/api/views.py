from rest_framework import generics
from .models import Todo
from .serialisers import TodoSerialiser
# from .mypagination import TodoPagination

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    # pagination_class = TodoPagination

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser