from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'message': 'Welcome my BBS',
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
      'message': 'Show Article' + str(id),
      'article': article,
    }
    return render(request, 'bbs/detail.html', context)

def create(request):
    article = Article(content='Hello BBS', user_name='paiza')
    article.save()

    articles = Article.objects.all()
    context = {
        'message': 'Create article',
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': 'Delete article ' + str(id),
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)