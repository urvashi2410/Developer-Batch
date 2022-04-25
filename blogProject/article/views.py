from django.shortcuts import render
from .models import Article 
from django.http import HttpResponse

# Create your views here.
def article(request):
    articles = Article.objects.all()
    data = {
        'articles' : articles 
    }
    return render(request, 'article.html', data)

def article_details(request, slug):
    return HttpResponse(slug)

def comment(request):
    return render(request, 'comment.html')