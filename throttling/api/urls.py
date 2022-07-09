from django.urls import path
from . import views

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>', views.SnippetRetrieve.as_view()),
    path('delete/<int:pk>', views.SnippetDestroy.as_view()),
    path('create/', views.SnippetCreate.as_view()),
    path('update/<int:pk>', views.SnippetUpdate.as_view())
]
