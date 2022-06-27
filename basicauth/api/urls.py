from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>', views.SnippetDetail.as_view())
]
