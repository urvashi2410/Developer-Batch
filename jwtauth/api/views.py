from rest_framework import generics
from .models import Todo
from .serialisers import TodoSerialiser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]