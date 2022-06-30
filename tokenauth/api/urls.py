from django.urls import path
from . import views 
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>', views.SnippetDetail.as_view()),
    path('tokenauth/', obtain_auth_token)
]