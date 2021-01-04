from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm

def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': 'Hello Django',
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
      'message': 'Show Article' + str(id),
      'article': article,
    }
    return render(request, 'bbs/detail.html', context)

def new(request):
  articleForm = ArticleForm()

  context = {
    'message': 'New Article',
    'articleForm': articleForm,
  }
  return render(request, 'bbs/new.html', context)

def create(request):
    article = Article(content='Hello BBS', user_name='paiza')
    article.save()

    articles = Article.objects.all()
    context = {
        'message': 'Create article',
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)

def edit(request, id):
  return HttpResponse('this is edit' + str(id))

def update(request, id):
  return HttpResponse('this is update' + str(id))

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': 'Delete article ' + str(id),
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)