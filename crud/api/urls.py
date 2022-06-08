from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_view),
    path('read/<int:pk>', views.read_view_particular),
    path('create/', views.create_view)
]
