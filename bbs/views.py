from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'message': 'Welcome my BBS',
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)