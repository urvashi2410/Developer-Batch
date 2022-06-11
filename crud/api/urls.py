from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.TodoClassBasedView().as_view()),
    path('todo/<int:pk>', views.TodoClassBasedView().as_view()),
]

'''
    path('read/', views.read_view),
    path('read/<int:pk>', views.read_view_particular),
    path('create/', views.create_view),
    path('update/<int:pk>', views.update_view),
    path('delete/<int:pk>', views.delete_view)
    '''