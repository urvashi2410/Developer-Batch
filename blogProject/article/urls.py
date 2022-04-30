from django.urls import path
from . import views 

urlpatterns = [
    path('', views.article, name='article_page'),
    path('comment/', views.comment),
    path('<slug:slug>/', views.article_details),
]