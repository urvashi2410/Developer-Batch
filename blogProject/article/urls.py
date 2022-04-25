from django.urls import path
from . import views 

urlpatterns = [
    path('', views.article),
    path('comment/', views.comment),
    path('<slug:slug>/', views.article_details),
]